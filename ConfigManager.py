#-*- coding:utf-8 -*-
import ConfigParser

class ConfigHandler:
    def __init__(self):
        self.confObj = ConfigParser.ConfigParser()
    
    # Attempt to read and parse a list of filenames
    # If filenames is a string or Unicode string, it is treated as a single filename.
    def loadConfig(self, conf_file_path):
        self.confObj.read(conf_file_path)
        
    # Write a representation of the configuration to the specified file object. 
    def exportConfig(self, conf_file_path):
        self.confObj.write(open(conf_file_path, 'wb'))
    
    # Return a list of the sections available
    def getSections(self):
        return self.confObj.sections() 
    
    # Indicates whether the named section is present in the configuration.
    def hasSection(self, section_name):
        return self.confObj.has_section(section_name)
    
    # Add a section named section to the instance.
    def addSection(self,section_name):
        # check the duplicated section by the given name already exists.
        if False == self.hasSection(section_name):
            self.confObj.add_section(section_name)
    
    # Remove the specified section from the configuration
    def rmSection(self,section_name):
        # If the section does not exist, do not any action.
        if True == self.hasSection(section_name):
            self.confObj.remove_section(section_name)
        
    # Returns a list of options available in the specified section.
    def getOptions(self,section_name):
        return self.confObj.options(section_name)
    
    # Return a list of (name, value) pairs for each option in the given section.
    def getItems(self, section_name):
        return self.confObj.items(section_name)
    
    # If the given section exists, and contains the given option, return True; 
    # otherwise return False.
    def hasOption(self, section_name, option_name):
        if True == self.hasSection(section_name):
            return self.confObj.has_option(section_name, option_name)
        else:
            return False
    
    # Remove the specified option from the specified section.
    def rmOption(self, section_name, option_name):
        # If the section & option does not exist, do not any action.
        if True == self.hasOption(section_name, option_name):
            self.confObj.remove_option(section_name, option_name)
    
    # Get an option value for the named section
    def getConfValue(self, section_name, option_name):
        if True == self.hasOption(section_name, option_name):
            return self.confObj.get(section_name, option_name)
       
    def getRowConfVal(self, section_name, option_name):
        if True == self.hasOption(section_name, option_name):
            return self.confObj.get(section_name, option_name, 1)
        
    # return item by user given type
    def getConfValueByType(self, section_name, option_name, value_type):
        if True == self.hasOption(section_name, option_name):
            # integer
            if value_type == "int":
                return self.confObj.getint(section_name, option_name)
            # floating point number.
            elif value_type == "float":
                return self.confObj.getfloat(section_name, option_name)
            # Boolean value.
            # True :  "1", "yes", "true", and "on"
            # False : "0", "no", "false", and "off"
            elif value_type == "float":
                return self.confObj.getboolean(section_name, option_name)
        
    # If the given section exists, set the given option to the specified value
    def setConfValue(self, section_name, option_name, value):
        self.confObj.set(section_name, option_name, value)
        
if __name__ == "__main__":
    print "Start"
    config = ConfigHandler()
    config.loadConfig("test.conf")
    print config.getItems("Test")