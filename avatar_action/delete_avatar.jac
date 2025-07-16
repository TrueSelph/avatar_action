import from jivas.agent.core.agent { Agent }
import from jivas.agent.action.action { Action }
import from jivas.agent.action.actions { Actions }
import from jivas.agent.action.agent_graph_walker { agent_graph_walker }


walker delete_avatar(agent_graph_walker) {

    has response:str = None;

    can on_agent with Agent entry {
        visit [-->](`?Actions);
    }

    can on_actions with Actions entry {
        visit [-->](`?Action)(?enabled==True)(?label=='AvatarAction');
    }

    can on_action with Action entry {
        self.response = here.delete_avatar_image();
    }

}