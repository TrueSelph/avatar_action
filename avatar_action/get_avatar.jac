import:py base64;
import:jac from jivas.agent.core.agent { Agent }
import:jac from jivas.agent.action.action { Action }
import:jac from jivas.agent.action.actions { Actions }
import:jac from jivas.agent.action.interact_graph_walker { interact_graph_walker }


walker get_avatar :interact_graph_walker: {

    has base64_prefix:bool = True;
    has response:str = None;

    can on_agent with Agent entry {
        visit [-->](`?Actions);
    }

    can on_actions with Actions entry {
        visit [-->](`?Action)(?enabled==True)(?label=='AvatarAction');
    }

    can on_action with Action entry {
        self.response = here.get_avatar_image(self.base64_prefix);
    }

}