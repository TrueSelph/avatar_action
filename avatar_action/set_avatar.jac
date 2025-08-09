import logging;
import from logging { Logger }
import base64;
import from jivas.agent.core.agent { Agent }
import from jivas.agent.action.action { Action }
import from jivas.agent.action.actions { Actions }
import from jivas.agent.modules.action.path { action_walker_path }
import from jivas.agent.action.agent_graph_walker { agent_graph_walker }


walker set_avatar(agent_graph_walker) {

    has files:list[dict] = [];
    has response:bool = False;
    has reporting:bool = True;

    # set up logger
    static has logger:Logger = logging.getLogger(__name__);

    class __specs__ {
        static has private: bool = False;
        static has path: str = action_walker_path(__module__);
    }

    can on_agent with Agent entry {
        visit [-->](`?Actions);
    }

    can on_actions with Actions entry {
        visit [-->](`?Action)(?enabled==True)(?label=='AvatarAction');
    }

    can on_action with Action entry {
        if self.files {

            for file in self.files {
                if( file.get("content")) {
                    self.response = here.set_avatar_image(image_data = file.get("content"), mimetype = file['type']);
                }
            }
        }

        if self.reporting {
            report self.response;
        }
    }

}