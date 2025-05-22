```json
{
    "mcp": {
        "inputs": [],
        "servers": {
            "mcp-notification": {
                "command": "uv",
                "args":[
                    "--directory",
                    "<PATH>",
                    "run",
                    "main.py"
                ],
                "env": {
                    "BOT_TOKEN": "<TOKEN>"
                }
            }
        }
    }
}
```