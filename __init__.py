import server
from aiohttp import web

# Define the route registration function
def setup_routes():
    # Get the PromptServer instance routes
    routes = server.PromptServer.instance.routes
    
    # Register a new GET route
    @routes.get("/test/hello")
    async def test_hello(request):
        return web.json_response({
            "message": "Hello from ComfyUI-Test-Plugin!",
            "status": "success"
        })

# Call the setup function to register routes when the module is imported
setup_routes()

# Standard ComfyUI custom node exports
NODE_CLASS_MAPPINGS = {}
__all__ = ['NODE_CLASS_MAPPINGS']
