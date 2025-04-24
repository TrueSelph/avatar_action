"""Streamlit app for managing agent avatar actions."""

import uuid

import streamlit as st
from jvcli.client.lib.utils import call_action_walker_exec, decode_base64_image
from jvcli.client.lib.widgets import app_header, app_update_action
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
                    call_action_walker_exec(agent_id, module_root, "delete_avatar")
                    st.session_state[model_key]["image_data"] = None
                    st.rerun()

    # we need a new uploader key per upload to completely reset the upload control once we're done with it
    if "uploader_key" not in st.session_state:
        st.session_state.uploader_key = f"{str(uuid.uuid4())}_file_uploader"

    selected_file = st.file_uploader(
        "Choose an image file",
        type=["jpg", "png", "jpeg"],
        key=st.session_state.uploader_key,
    )

    if selected_file is not None:
        # Display the uploaded image
        st.image(selected_file, caption="image preview", width=200)

        upload_container = st.container()
        with upload_container:
            if st.button("Upload"):
                with st.spinner("Uploading avatar, please wait..."):
                    # Prepare list of files if any are uploaded
                    files_list = []
                    if selected_file:
                        files_list.append(
                            (
                                selected_file.name,
                                selected_file.read(),
                                selected_file.type,
                            )
                        )

                    # Call the function to add the new text document
                    if call_set_avatar(agent_id, module_root, files_list):
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


def call_set_avatar(agent_id: str, module_root: str, files: list) -> bool:
    """Set the avatar for the agent by calling the set_avatar action."""
    return call_action_walker_exec(agent_id, module_root, "set_avatar", None, files)
