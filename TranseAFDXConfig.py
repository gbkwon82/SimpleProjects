#-*- coding:utf-8 -*-

import datetime
import XmlParser

# import user module
import DateUtility
import FileManager
import ConfigManager
import LoggingManager

import AfdxSwitchConfigFileForm as afdxForm

class AFDXConfigGenerator:
    def __init__(self):
        self.logMng = LoggingManager.LogHandler("CfgGen")
        self.logMng.logLevel("DEBUG")
        self.logMng.attachedStreamHandler()
        self.logMng.attachedFileHandler("CfgGen.log")
        self.logMng.infoMesg("Initialize AFDXConfigGenerator")
        
        self.configMng = ConfigManager.ConfigHandler()
        self.configMng.loadConfig("afdx_switch.conf")
        
        self.xmlParserMng = XmlParser.XmlParser()
        
        self.switchPortInfoList = []
        self.smfdCfgFileList = []
        self.smfdAfdxCfgPathDict = {}
        
        self.loadAFDXSwitchInfo()
    
    # 파일 실행 날짜 및 시간을 반환함
    def getCurrentTime(self):
        nowTime = datetime.datetime.now()
        return nowTime.strftime("%Y.%m.%d %H:%M:%S")

    # 장비별 AFDX Switch port 정보를 리스트 타입으로 로드함 
    def loadAFDXSwitchInfo(self):
        self.switchPortInfoList = self.configMng.getItems("AFDX_SWITCH_PORT")
    
    def readSMFDConfigFiles(self):
        smfd_cfg_path = self.configMng.getConfValue("PATH", "SMFD_AFDX_CFG_FOLDER")
        smfd_cfg_files = self.configMng.getItems("SMFD_AFDX_CFG_FILES")
        smfd_cfg_path = FileManager.joinPath(FileManager.getCurrentPath(), smfd_cfg_path)
        
        self.logMng.infoMesg("Read SMFD config files")
        for (smfd_id, cfg_file_name) in smfd_cfg_files:
            self.logMng.infoMesg("Read %s", cfg_file_name)
            self.smfdAfdxCfgPathDict[smfd_id] = {}
            self.smfdAfdxCfgPathDict[smfd_id]["path"] = FileManager.joinPath(smfd_cfg_path, cfg_file_name)
            self.smfdAfdxCfgPathDict[smfd_id]["xml"] = XmlParser.XmlParser()
            self.smfdAfdxCfgPathDict[smfd_id]["xml"].makeNormalizeXmlFile(self.smfdAfdxCfgPathDict[smfd_id]["path"])
        
    # AFDX Switch Config 파일의 전역 설정값을 반환함
    def getCfgFileGlobalDefStr(self, afdx_file_name):
        self.logMng.infoMesg("Global Config set with %s" % afdx_file_name)
        return afdxForm.getCfgFileGlobal(self.getCurrentTime(), afdx_file_name)

    # AFDX Switch의 포트별 설정을 반환함   
    def getPortTableStr(self):
        portTableStr = ""
        for portInfo in self.switchPortInfoList:
            portTableStr = portTableStr + afdxForm.getPort(portInfo[1],"1000","1","256","256")
        
        portTableStr = afdxForm.getPortTable(portTableStr)
        return portTableStr
    
    def getVlLinkTableStr(self):
        smfd_cfg_ports = self.configMng.getItems("AFDX_SWITCH_PORT")
        vlLinkTbDict = {}
        virtualLinkDefStr = ""
        for (smfd_id, port_no) in smfd_cfg_ports:        
            xmlETMng = self.smfdAfdxCfgPathDict[smfd_id]["xml"]
            xmlETMng.xmlParsing()
            txVlSubElemntList = xmlETMng.findAll("TxVL")
            if txVlSubElemntList is None:
                self.logMng.infoMesg("AFDX config file is invalid")
            else:
                # XML 파일을 파싱하여 Switch 설정 파일에 필요한 정보 수집
                for subTxVlElemnt in txVlSubElemntList:
                    subVlElement = xmlETMng.find("SubVL", subTxVlElemnt)
                    txPortElement = xmlETMng.find("TxPort", subVlElement)
                    
                    vlId = subTxVlElemnt.attrib['VL_ID']
                    inPort = port_no
                    outPort = txPortElement.find("DST_L_ID").text
                    outPort = self.configMng.getConfValue("AFDX_SWITCH_PORT", "SMFD%s"%outPort)
                    bag = xmlETMng.find("BAG_TIME", subTxVlElemnt).text
                    
                    if vlLinkTbDict.has_key(vlId) is True:
                        if vlLinkTbDict[vlId]["rx"] == inPort:
                            vlLinkTbDict[vlId]["tx"].append(outPort)
                        else:
                            vlLinkTbDict[vlId] = {"rx":inPort, "out":[outPort,],"bag":bag}
                    else:
                        vlLinkTbDict[vlId] = {"rx":inPort, "tx":[outPort,],"bag":bag}
                        
        # 수집된 정보를 바탕으로 Virtual Link Table 설정 파일 작성
        vlIdList = vlLinkTbDict.keys()
        vlIdList.sort()
        virtualLinkTableDefStr = ""
        for vlId in vlIdList:
            id = vlId
            rxPort = vlLinkTbDict[vlId]["rx"]
            txPortList = vlLinkTbDict[vlId]["tx"]
            bag = vlLinkTbDict[vlId]["bag"] + "00"
            jitter = "10"
            virtualLinkDefStr = virtualLinkDefStr + afdxForm.getVirtualLink(id, rxPort, txPortList, bag, jitter)
                
        virtualLinkTableDefStr = afdxForm.getVirtualLinkTable(virtualLinkDefStr)
        return virtualLinkTableDefStr
                
                
    def makeSwitchCfgFile(self):
        self.readSMFDConfigFiles()
        
        fileName = self.configMng.getConfValue("PATH", "SWITCH_CFG_FILE_NAME")
        fileName = "_".join([fileName, DateUtility.getTodayStr("%y%m%d")])

        cfgFp = open(fileName,"w")
        cfgFp.write(self.getCfgFileGlobalDefStr(fileName))
        cfgFp.close()
    
if __name__ == "__main__" :
    test = AFDXConfigGenerator()
#     print test.getCurrentTime()
#     print test.getCfgFileGlobalDefStr("AFDX_SWITCH_1")
#     test.getPortDefStr()
#     test.readSMFDConfigFiles()
#     print test.getVlLinkTable()
    test.makeSwitchCfgFile()