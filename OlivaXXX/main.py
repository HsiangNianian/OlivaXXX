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
    def init(plugin_event, Proc):
        pass
    
    def private_message(plugin_event,Proc):
        util(plugin_event,Proc)
        
    def group_message(plugin_event,Proc):
        util(plugin_event,Proc)
                    
    def save(plugin_event, Proc):
        pass

    def menu(plugin_event, Proc):
        if plugin_event.data.namespace == 'DailyNews':  # type: ignore
            if plugin_event.data.event == 'Menu_Config':  # type: ignore
                logg("有笨蛋打开了配置")
            elif plugin_event.data.event == 'Menu_About':  # type: ignore
                pass
             
                                    
def util(plugin_event,Proc):
    msg = plugin_event.data.message
    if msg == "test":
        plugin_event.reply("BAKA")
