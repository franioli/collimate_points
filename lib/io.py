import numpy as np
import pandas as pd

import Metashape


def write_markers_by_camera(chunk: Metashape.Chunk,
                            file_name: str,
                            convert_to_micron: bool = False,
                            ) -> None:
    """ Write Marker image coordinates to csv file,
    sort by camera, as follows:
    cam1, marker1, x, y
    cam1, marker2, x, y
    ... 
    cam1, markerM, x, y
    cam2, marker1, x, y
    ....
    camN, markerM, x,Y

    Args:
        chunk (Metashape.Chunk): Metashape Chunk
        file_name (str): path of the output csv file
        convert_to_micron (bool, default = False) 
    """

    # Write header to file
    file = open(file_name, "w")

    # If convert_to_micron is True, convert image coordinates from x-y (row,column) image coordinate system to xi-eta image coordinate system (origin at the center of the image, xi towards right, eta upwards)
    if convert_to_micron:
        file.write("image_name,feature_id,xi,eta\n")
    else:
        file.write("image_name,feature_id,x,y\n")

    for camera in chunk.cameras:
        for marker in chunk.markers:
            projections = marker.projections  # list of marker projections
            marker_name = marker.label

            for cur_cam in marker.projections.keys():
                if cur_cam == camera:
                    cam_name = cur_cam.label
                    x, y = projections[cur_cam].coord

                    # writing output to file
                    if convert_to_micron:
                        pixel_size_micron = cur_cam.sensor.pixel_size * 1000
                        image_width = cur_cam.sensor.width
                        image_heigth = cur_cam.sensor.height
                        xi = (x - image_width/2) * pixel_size_micron[0]
                        eta = (image_heigth/2 - y) * pixel_size_micron[1]
                        file.write(
                            f"{cam_name},{marker_name:5},{xi:8.1f},{eta:8.1f}\n"
                        )
                    else:
                        file.write(
                            f"{cam_name},{marker_name},{x:.4f},{y:.4f}\n"
                        )

    file.close()
    print("Marker exported successfully")


def write_markers_by_marker(chunk: Metashape.Chunk,
                            file_name: str,
                            ) -> None:
    """ Write Marker image coordinates to csv file,
    sort by camera, as follows:
    marker1, cam1, x, y
    marker1, cam2, x, y
    ... 
    marker1, camN, x, y
    marker2, cam1, x, y
    ....
    markerM, camN, x, y

    Args:
        chunk (Metashape.Chunk): Metashape Chunk
        file_name (str): path of the output csv file
    """

    file = open(file_name, "w")

    for marker in chunk.markers:
        projections = marker.projections  # list of marker projections
        marker_name = marker.label
        for camera in marker.projections.keys():
            x, y = projections[camera].coord
            label = camera.label
            # writing output to file
            file.write(f"{marker_name},{label},{x:.4f},{y:.4f}\n")

    file.close()
    print("Marker exported successfully")


def write_marker_world_coordinates(chunk: Metashape.Chunk,
                                   file_name: str,
                                   ) -> None:
    """ Write Marker world coordinates to csv file as:
    marker1, X, Y, Z    
    ... 
    markerM, X, Y, Z    

    Args:
        chunk (Metashape.Chunk): Metashape Chunk
        file_name (str): path of the output csv file
    """

    file = open(file_name, "w")

    for marker in chunk.markers:
        marker_name = marker.label
        X, Y, Z = marker.reference.location
        # writing output to file
        file.write(f"{marker_name:5},{X:15.4f},{Y:15.4f},{Z:15.4f}\n")

    file.close()
    print("Marker exported successfully")
