import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

import Metashape 

from easydict import EasyDict as edict

from lib.io import (write_markers_by_camera, 
                    write_markers_by_marker, 
                    write_marker_world_coordinates,
                    )
from lib.utils import check_license

check_license()


load_project = "data/belpy.psx"
project_file = "data/belpy_new.psx"
# markers_file = "data/belpy_markers.csv"

# create a handle to the Metashape object
# When running via Metashape, can use: doc = Metashape.app.document
doc = Metashape.Document()

# If specified, open existing project
if load_project != "":
    doc.open(load_project)
else:
    # Initialize a chunk, set its CRS as specified
    chunk = doc.addChunk()
    # chunk.crs = Metashape.CoordinateSystem(cfg["project_crs"])
    # chunk.marker_crs = Metashape.CoordinateSystem(
    #     cfg["addGCPs"]["gcp_crs"])

# Save doc doc as new project (even if we opened an existing project, save as a separate one so the existing project remains accessible in its original state)
doc.save(project_file)

chunk = doc.chunk
write_markers_by_camera(chunk, "data/belpy2807_markers_images.csv", 
                        convert_to_micron=False)
# write_marker_world_coordinates(chunk, "data/belpy2807_markers_world.csv")


from pathlib import Path

def write_markers_one_cam_per_file( chunk: Metashape.Chunk,
                                    output_dir = 'targets',
                                    convert_to_micron: bool = False,
                                    ) -> None:
    """ Write Marker image coordinates to csv file,
    sort by camera, as follows:
    marker1, x, y
    marker2, x, y
    ... 
    markerM, x, y

    Args:
        chunk (Metashape.Chunk): Metashape Chunk
        output_dir (str): path of the output folder (default="targets")
        convert_to_micron (bool, default = False) 
    """

    # Check if output folder exists, or create it
    output_dir = Path(output_dir)
    
    if not (output_dir.is_dir()):
        print("Output directory does not exists. Creating it.")
        output_dir.mkdir()
    else:
        print("Output directory already exists. Writing files in it.")

    for camera in chunk.cameras:
        
        # Write header to file
        file = open(output_dir / (camera.label+'.csv'), 'w')
        file.write("label,x,y\n")

        for marker in chunk.markers:
            projections = marker.projections  # list of marker projections
            marker_name = marker.label

            for cur_cam in marker.projections.keys():
                if cur_cam == camera:
                    cam_name = cur_cam.label
                    x, y = projections[cur_cam].coord

                    # writing output to file
                    file.write(f"{marker_name},{x:.4f},{y:.4f}\n")
        file.close()

    print("All targets exported successfully")


write_markers_one_cam_per_file( chunk, 
                                "targets",
                                convert_to_micron=False)



