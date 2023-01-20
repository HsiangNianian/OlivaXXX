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
import OlivaGithub
from OlivaGithub.github import GitHub

gh = GitHub(token="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")
    
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
             
                                     
"""
// Octokit.js
// https://github.com/octokit/core.js#readme
const octokit = new Octokit({
  auth: 'YOUR-TOKEN'
})

await octokit.request('POST /orgs/{org}/repos', {
  org: 'ORG',
  name: 'Hello-World',
  description: 'This is your first repository',
  homepage: 'https://github.com',
  'private': false,
  has_issues: true,
  has_projects: true,
  has_wiki: true
})
"""

def util(plugin_event,Proc):
    # @
    msg = plugin_event.data.message
    if msg == "test":
        r = gh.repos("HsiangNianian")("OlivaGithub").repos.post(dict(name="OlivaGithub",decsription="一个简单的github推送插件",has_issues=True))
        #r = gh.repos('HsiangNianian')('OlivaGithub').issues.post(title='issues 10', body='#10', assignees=['HsiangNianian','BalugaLand'])
        plugin_event.reply(str(gh.x_ratelimit_limit)+r.title)