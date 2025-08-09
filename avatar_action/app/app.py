"""Streamlit app for managing agent avatar actions."""

import base64
import uuid

import streamlit as st
from jvclient.lib.utils import call_api, decode_base64_image, get_reports_payload
from jvclient.lib.widgets import app_header, app_update_action
from streamlit_router import StreamlitRouter


def render(router: StreamlitRouter, agent_id: str, action_id: str, info: dict) -> None:
    """Render the UI for avatar actions in the Streamlit web app."""
    # Add application header controls
    (model_key, module_root) = app_header(agent_id, action_id, info)

    # render the avatar image if there is one...
    if st.session_state[model_key]["image_data"]:
        st.image(
            decode_base64_image(st.session_state[model_key]["image_data"]),
            caption="image preview",
            width=200,
        )

        # Batch the button and spinner in a container so the spinner appears near the button
        delete_container = st.container()
        with delete_container:
            if st.button("Delete Avatar"):
                with st.spinner("Deleting avatar, please wait..."):
                    call_api(
                        endpoint="action/walker/avatar_action/delete_avatar",
                        json_data={"agent_id": agent_id},
                    )
                    st.session_state[model_key]["image_data"] = None
                    st.rerun()

    # we need a new uploader key per upload to completely reset the upload control once we're done with it
    if "uploader_key" not in st.session_state:
        st.session_state.uploader_key = f"{str(uuid.uuid4())}_file_uploader"

    selected_file = st.file_uploader(
        "Choose an image file",
        type=["jpg", "png", "jpeg"],
        key=st.session_state.uploader_key,
        accept_multiple_files=False,
    )

    if selected_file is not None:
        # Display the uploaded image
        st.image(selected_file, caption="image preview", width=200)

        upload_container = st.container()
        with upload_container:
            if st.button("Upload"):
                with st.spinner("Uploading avatar, please wait..."):
                    # Read the file data
                    file_bytes = selected_file.read()
                    mimetype = selected_file.type
                    
                    # Encode the bytes to base64 and format as data URI
                    encoded_data = base64.b64encode(file_bytes).decode('utf-8')
                    
                    # Make the API call with properly formatted data
                    result = call_api(
                        endpoint="action/walker/avatar_action/set_avatar",
                        json_data={
                            "agent_id": agent_id, 
                            "files": [{
                                "content": encoded_data,
                                "type": mimetype
                            }]
                        },
                    )

                    if result and result.status_code == 200:
                        # Remove uploader_key to hide the preview on success
                        del st.session_state["uploader_key"]
                        # Remove the model_key to refresh the model
                        del st.session_state[model_key]
                        # now reload
                        st.rerun()
                    else:
                        st.error("Failed to add avatar")    
                    
    # Add update button to apply changes
    app_update_action(agent_id, action_id)


