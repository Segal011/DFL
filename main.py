

if __name__ == "__main__":
    print("TTRRRTTT")

    from functions import Functions
    import os
    import sys
    import argparse

    from argparse import Namespace
    # Fix for linux
    # import multiprocessing
    # multiprocessing.set_start_method("spawn")

    from core.leras import nn
    nn.initialize_main_env()

    exit_code = 0

    # Create the config object with default values and comments for each argument
    config = Namespace(
        add_landmarks_debug_images=False, # Add landmarks debug image for aligned faces.
        aligned_dir=None, # Aligned directory. This is where the extracted of dst faces stored.
        audio_track_id=None, # Specify audio track id.
        bitrate=None, # Bitrate of output file in Megabits.
        cpu_only=False, # Train on CPU.
        debug=False, # Debug samples.
        detector='s3fd', #['s3fd','manual']
        execute_program=[], # Execute program.
        ext='jpeg', # Image format (extension) of input files
        export_faceset_mask=False, # Export faceset mask.
        face_type='whole_face', # ['half_face', 'full_face', 'whole_face', 'head', 'mark_only']
        factor=10, # Denoise factor (1-20)
        force_gpu_idxs=[0], # Force to choose GPU indexes separated by comma.
        force_model_name=None, # Forcing to choose model name from model/ folder.
        from_time=None, # From time, for example 00:00:00.000
        fps=0, # Extract 30 frames of every second of the video
        include_audio=False, # Include audio from reference file
        input_dir="workspace_small/data_src/", # Input directory. A directory containing the files you wish to process.
        input_file='workspace/data_src.mp4', # Input file to be processed
        lossless=False, # Whether to use the PNG codec for lossless compression
        manual_fix=False,
        manual_output_debug_fix=False,
        model_dir='LIAE_04-01', # Saved models dir.
        model_name='SAEHD', # Model class name.
        no_preview=False, # Disable preview window.
        output_debug=False,#
        output_dir="workspace_small/data_dst/", # Output directory. This is where the merged files will be stored.
        output_ext='jpg', # Image format (extension) of output files
        output_file='workspace/data_dst.mp4', # Output file to be created
        output_mask_dir=None, # Output mask directory. This is where the mask files will be stored.
        pack_faceset=False, # Pack faceset.
        # pretraining_data_dir=None,
        # pretrained_model_dir=None,
        pretraining_data_dir='/data/notebook_files/LIAE/512wf_SAEHD_data.dat', # Optional dir of extracted faceset that will be used in pretraining mode.
        pretrained_model_dir='/data/notebook_files/LIAE', # Optional dir of pretrain model files. (Currently only for Quick96).
        recover_original_aligned_filename=False, # Recover original aligned filename.
        reference_file='/path/to/reference/video.mp4', # Reference file used to determine FPS and transfer audio
        restore_faceset_metadata=False, # Restore faceset metadata to file. Image filenames must be the same as used with save.
        save_faceset_metadata=False, # Save faceset metadata to file.
        silent_start=True, # Silent start. Automatically chooses Best GPU and last used model.
        sort_by_method=None, # Method of sorting. 'origname' sort by original filename to recover original sequence.
        to_time=None, # To time, for example 00:00:00.000
        training_data_dst_dir='workspace/data_dst/aligned', # Dir of extracted DST faceset.
        training_data_src_dir='workspace/data_src/aligned', # Dir of extracted SRC faceset.


        unpack_faceset=False, # Unpack faceset.

        jpeg_quality=50,
        manual_window_size=1368,
        max_faces_from_image=1,
        image_size=512,
    )


    # create an ArgumentParser object
    parser = argparse.ArgumentParser(description='My Python script')
    # add an argument to the parser
    parser.add_argument('--task', type=str, help='Task')
    # parse the command-line arguments
    args = parser.parse_args()

    print(f"Task: {args.task}" )

    obj = Functions()
    method = getattr(obj, args.task)
    method(config)

    if exit_code == 0:
        print("Done.")
        
    exit(exit_code)
    
