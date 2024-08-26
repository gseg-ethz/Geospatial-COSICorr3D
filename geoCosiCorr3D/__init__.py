import os
import geoCosiCorr3D.geoCore.constants as C


def update_ld_library_path():
    # Define the path to the shared libraries
    new_lib_path = C.GEOCOSICORR3D_LIB_DIR

    # Get the current LD_LIBRARY_PATH
    current_ld_library_path = os.environ.get('LD_LIBRARY_PATH', '')

    # Check if the new_lib_path is already in LD_LIBRARY_PATH
    if new_lib_path not in current_ld_library_path.split(':'):
        # Add your path to LD_LIBRARY_PATH
        if current_ld_library_path:
            new_ld_library_path = f"{new_lib_path}:{current_ld_library_path}"
        else:
            new_ld_library_path = new_lib_path

        # Update the environment variable
        os.environ['LD_LIBRARY_PATH'] = new_ld_library_path

# Call the function when the package is imported
# update_ld_library_path()


if not os.path.exists(C.SOFTWARE.WKDIR):
    os.makedirs(C.SOFTWARE.WKDIR)

