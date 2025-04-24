import:py logging;
import:py traceback;
import:py from typing { Union, Optional }
import:py from logging { Logger }
import:jac from jivas.agent.action.action { Action }

node AvatarAction :Action: {
    # Registers a cron-like job to trigger agent actions on an interval.

    # set up logger
    static has logger:Logger = logging.getLogger(__name__);

    has image_data:str = "";
    has mimetype:str = "";

    can set_avatar_image(image_data:str, mimetype:str) -> bool {
        # sets the image data and mimetype, updates agent

        self.image_data = image_data;
        self.mimetype = mimetype;

        # update the agent
        if(self.get_agent().update()) {
            return True;
        }
        return False;
    }

    can get_avatar_image(with_prefix:bool = True) -> Optional[str] {
        # returns the base64 encoded avatar image, with or without prefix

        if not self.image_data {
            return None;
        }
        if with_prefix {
            return f"data:{mimetype};base64,{self.image_data}";
        }
        return self.image_data;
    }

    can delete_avatar_image() -> bool {
        # deletes the avatar image data

        self.image_data = "";
        self.mimetype = "";

        # update the agent
        if(self.get_agent().update()) {
            return True;
        }
        return False;
    }

    can healthcheck() -> Union[bool, dict] {

        if(not self.image_data){
            return {
                "status": True,
                "message": "Avatar image is not set.",
                "severity": "warning"
            };
        }
        return True;

    }

}