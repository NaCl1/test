import os
import sys

# Ensure ComfyUI root is in sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
comfy_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if comfy_root not in sys.path:
    sys.path.insert(0, comfy_root)

try:
    import server
    from aiohttp import web
except ImportError:
    print("Warning: Could not import ComfyUI server modules.")
    server = None
    web = None

def setup_dynamic_route():
    if server is None or web is None:
        print("Skipping route registration due to missing modules.")
        return

    try:
        # Access the PromptServer instance
        # Note: When running as a subprocess, this instance will be None or distinct from the main process
        instance = server.PromptServer.instance
        
        if instance is None:
            print("PromptServer.instance is None. Initializing a new instance or skipping.")
            # In a real subprocess, we can't affect the main process memory. 
            # This code assumes it might be running in a context where it can access the server,
            # or it demonstrates the logic intended by the user.
            return

        # Define the route handler
        async def install_route_handler(request):
            return web.json_response({
                "message": "Route added dynamically via install.py",
                "status": "success"
            })

        # Register the route
        print("Attempting to register dynamic route...")
        
        # Method 1: Add to routes table (for future app startup)
        instance.routes.get("/test/install_route")(install_route_handler)
        
        # Method 2: Add directly to running app router (if app is already running)
        if hasattr(instance, 'app') and instance.app is not None:
            instance.app.router.add_get("/test/install_route", install_route_handler)
            print("Successfully added route /test/install_route to running application.")
        else:
            print("PromptServer app instance not found. Route added to definitions only.")

    except Exception as e:
        print(f"Failed to register dynamic route: {e}")

if __name__ == "__main__":
    print("Executing install.py logic...")
    setup_dynamic_route()
    print("install.py execution completed.")
