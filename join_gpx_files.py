"""
Script for joining multiple FPX files downloaded from Strava.

Usage:      python join_gpx_files.py [gpx_directory] [output_file.gpx]
Example:    python join_gpx_files.py gpx_from_workouts output.gpx
"""

import sys
import glob
import os

head_file = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\" ?>\n \
<gpx xmlns=\"http://www.topografix.com/GPX/1/1\" creator=\"\" version=\"1.1\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd\">\n"

foot_file = "</gpx>"

if __name__ == '__main__':
    try:
        gpx_directory, output_file = sys.argv[1:3]
    except:
        sys.exit('Usage: python %s files output_file.gpx' % sys.argv[0])

    files_to_join = glob.glob(os.path.join(gpx_directory, '*.gpx'))
    print(f'Found {len(files_to_join)} GPX files to join')

    final_file = open(output_file, 'w')
    final_file.write(head_file)

    for file in files_to_join:
        try:
            gpx_read = open(file, 'r')
            gpx_file_txt = gpx_read.read()

            track_segment = gpx_file_txt[(gpx_file_txt.index('<trk>')):]
            track_segment = track_segment[:(track_segment.index('</trk>') + 6)] + "\n"
        except:
            print('Unexpected error:', sys.exc_info()[0])
            sys.exit('Problems in %s' % file)

    final_file.write(foot_file)
    final_file.close()
    print('Done')