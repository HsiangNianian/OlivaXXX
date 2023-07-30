# -*- encoding: utf-8 -*-
'''
     ██╗██╗   ██╗██╗   ██╗███╗   ██╗██╗  ██╗ ██████╗ 
     ██║╚██╗ ██╔╝██║   ██║████╗  ██║██║ ██╔╝██╔═══██╗
     ██║ ╚████╔╝ ██║   ██║██╔██╗ ██║█████╔╝ ██║   ██║
██   ██║  ╚██╔╝  ██║   ██║██║╚██╗██║██╔═██╗ ██║   ██║
╚█████╔╝   ██║   ╚██████╔╝██║ ╚████║██║  ██╗╚██████╔╝
 ╚════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ 
                                                     
    Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
import OlivOS
import OlivaXXX

class Event(object):
    def init(self, Proc):
        pass
    
    def private_message(self, Proc):
        util(self, Proc)
        
    def group_message(self, Proc):
        util(self, Proc)
                    
    def save(self, Proc):
        pass

    def menu(self, Proc):
        if self.data.namespace == 'DailyNews':  # type: ignore
            if self.data.event == 'Menu_Config':  # type: ignore
                logg("有笨蛋打开了配置")
             
                                    
def util(plugin_event,Proc):
    msg = plugin_event.data.message
    if msg == "test":
        plugin_event.reply("BAKA")
