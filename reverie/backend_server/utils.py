import os

# Fetch the OpenAI API Key from the environment variable
openai_api_key = os.environ.get('OPENAI_API_KEY', 'Default_Value_If_Not_Found')
# If you want the script to fail if the key is not set, you can use:
# openai_api_key = os.environ['OPENAI_API_KEY']

# Put your name
key_owner = os.environ.get('KEY_OWNER', 'Default_Name_If_Not_Found')
# If you want the script to fail if the name is not set, you can use:
# key_owner = os.environ['KEY_OWNER']

maze_assets_loc = "../../environment/frontend_server/static_dirs/assets"
env_matrix = f"{maze_assets_loc}/the_ville/matrix"
env_visuals = f"{maze_assets_loc}/the_ville/visuals"

fs_storage = "../../environment/frontend_server/storage"
fs_temp_storage = "../../environment/frontend_server/temp_storage"

collision_block_id = "32125"

# Verbose 
debug = True
