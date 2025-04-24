# Avatar Action

![GitHub release (latest by date)](https://img.shields.io/github/v/release/TrueSelph/avatar_action)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/TrueSelph/avatar_action/test-avatar_action.yaml)
![GitHub issues](https://img.shields.io/github/issues/TrueSelph/avatar_action)
![GitHub pull requests](https://img.shields.io/github/issues-pr/TrueSelph/avatar_action)
![GitHub](https://img.shields.io/github/license/TrueSelph/avatar_action)

This action is designed to permit the upload and serving of an avatar image for your agent.

## Package Information

- **Name:** `jivas/avatar_action`
- **Author:** [V75 Inc.](https://v75inc.com/)
- **Architype:** `AvatarAction`

## Meta Information

- **Title:** Avatar Action
- **Group:** core
- **Type:** action

## Configuration

- **Singleton:** true

## Dependencies

- **Jivas:** `^2.0.0`

---

## Avatar Action API

The Avatar Action supports avatar management for agents via a unified API endpoint. You can set, retrieve, and delete an agent's avatar image using the `set_avatar`, `get_avatar`, and `delete_avatar` walkers respectively.

### Endpoint

`POST /action/walker`

---

### Required Parameters

| Parameter     | Description                             | Example Value             |
|---------------|-----------------------------------------|---------------------------|
| agent_id      | The ID of the agent                     | `"my-agent-uuid"`         |
| module_root   | Module root for these actions           | `"actions.jivas.avatar_action"` |
| walker        | The operation to perform                | `"set_avatar"`            |
| args          | Arguments dictionary for the walker     | See examples below        |
| files         | List of file objects, required for upload operations | See below           |

---

## Walkers and Payload Examples

### 1. Set Avatar

**Walker:** `'set_avatar'`

- Uploads and sets an avatar image for the agent.
- The `files` parameter should include the image file to be set as the avatar.
- The image content needs to be base64-encoded on the backend.

#### Sample Payload
```json
{
    "agent_id": "my-agent-uuid",
    "module_root": "actions.jivas.avatar_action",
    "walker": "set_avatar",
    "args": {},
    "files": [
        {
            "name": "avatar.png",
            "content": "<binary image data>",
            "type": "image/png"
        }
    ]
}
```

---

### 2. Get Avatar

**Walker:** `'get_avatar'`

- Retrieves the avatar image for the agent as a base64 encoded string.
- You may specify whether to include a base64 prefix using `base64_prefix`.

#### Sample Payload
```json
{
    "agent_id": "my-agent-uuid",
    "module_root": "actions.jivas.avatar_action",
    "walker": "get_avatar",
    "args": {
        "base64_prefix": true
    },
    "files": []
}
```

---

### 3. Delete Avatar

**Walker:** `'delete_avatar'`

- Deletes the agent's avatar image.

#### Sample Payload
```json
{
    "agent_id": "my-agent-uuid",
    "module_root": "actions.jivas.avatar_action",
    "walker": "delete_avatar",
    "args": {},
    "files": []
}
```

---

## Notes

- The response structure will depend on the walker's implementation.
- For `set_avatar`, ensure the image file is properly encoded and the mimetype is correctly specified.
- For `get_avatar`, if `base64_prefix` is `True`, the returned string will include the mimetype prefix (e.g., `data:image/png;base64,`).
- Errors and status messages will be returned as part of the response.

---

### Best Practices
- Validate your API keys and model parameters before deployment.
- Test pipelines in a staging environment before production use.

---

## 🔰 Contributing

- **🐛 [Report Issues](https://github.com/TrueSelph/avatar_action/issues)**: Submit bugs found or log feature requests for the `avatar_action` project.
- **💡 [Submit Pull Requests](https://github.com/TrueSelph/avatar_action/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/TrueSelph/avatar_action
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details open>
<summary>Contributor Graph</summary>
<br>
<p align="left">
    <a href="https://github.com/TrueSelph/avatar_action/graphs/contributors">
        <img src="https://contrib.rocks/image?repo=TrueSelph/avatar_action" />
   </a>
</p>
</details>

## 🎗 License

This project is protected under the Apache License 2.0. See [LICENSE](../LICENSE) for more information.
