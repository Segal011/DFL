from core import osex
from pathlib import Path
from core.interact import interact as io

class Functions:

    @staticmethod
    def process_train(arguments):
        # osex.set_process_lowest_prio()
        print("TRRRRR")

        kwargs = {'model_class_name'         : arguments.model_name,
                  'saved_models_path'        : Path(arguments.model_dir),
                  'training_data_src_path'   : Path(arguments.training_data_src_dir),
                  'training_data_dst_path'   : Path(arguments.training_data_dst_dir),
                  'pretraining_data_path'    : Path(arguments.pretraining_data_dir) if arguments.pretraining_data_dir is not None else None,
                  'pretrained_model_path'    : Path(arguments.pretrained_model_dir) if arguments.pretrained_model_dir is not None else None,
                  'no_preview'               : arguments.no_preview,
                  'force_model_name'         : arguments.force_model_name,
                  'force_gpu_idxs'           : arguments.force_gpu_idxs,
                  'cpu_only'                 : arguments.cpu_only,
                  'silent_start'             : arguments.silent_start,
                  'execute_programs'         : [ [int(x[0]), x[1] ] for x in arguments.execute_program ],
                  'debug'                    : arguments.debug,
                  }
        from mainscripts import Trainer
        Trainer.main(**kwargs)

    @staticmethod
    def process_exportdfm(arguments):
        osex.set_process_lowest_prio()
        from mainscripts import ExportDFM
        ExportDFM.main(
            model_class_name = arguments.model_name,
            saved_models_path = Path(arguments.model_dir)
        )

    @staticmethod
    def process_merge(arguments):
        osex.set_process_lowest_prio()
        from mainscripts import Merger
        Merger.main (model_class_name       = arguments.model_name,
                     saved_models_path      = Path(arguments.model_dir),
                     force_model_name       = arguments.force_model_name,
                     input_path             = Path(arguments.input_dir),
                     output_path            = Path(arguments.output_dir),
                     output_mask_path       = Path(arguments.output_mask_dir),
                     aligned_path           = Path(arguments.aligned_dir) if arguments.aligned_dir is not None else None,
                     force_gpu_idxs         = arguments.force_gpu_idxs,
                     cpu_only               = arguments.cpu_only)

    @staticmethod
    def process_videoed_extract_video(arguments):
        osex.set_process_lowest_prio()
        from mainscripts import VideoEd
        VideoEd.extract_video (arguments.input_file, arguments.output_dir, arguments.output_ext, arguments.fps)

    @staticmethod
    def process_videoed_cut_video(arguments):
        osex.set_process_lowest_prio()
        from mainscripts import VideoEd
        VideoEd.cut_video (arguments.input_file,
                           arguments.from_time,
                           arguments.to_time,
                           arguments.audio_track_id,
                           arguments.bitrate)

    @staticmethod
    def process_videoed_denoise_image_sequence(arguments):
        osex.set_process_lowest_prio()
        from mainscripts import VideoEd
        VideoEd.denoise_image_sequence(Path(arguments.input_dir), arguments.factor)


    @staticmethod
    def process_videoed_video_from_sequence(arguments):
        osex.set_process_lowest_prio()
        from mainscripts import VideoEd
        VideoEd.video_from_sequence (input_dir      = arguments.input_dir,
                                     output_file    = arguments.output_file,
                                     reference_file = arguments.reference_file,
                                     ext      = arguments.ext,
                                     fps      = arguments.fps,
                                     bitrate  = arguments.bitrate,
                                     include_audio = arguments.include_audio,
                                     lossless = arguments.lossless)

    @staticmethod
    def process_faceset_enhancer(arguments):
        osex.set_process_lowest_prio()
        from mainscripts import FacesetEnhancer
        FacesetEnhancer.process_folder (Path(arguments.input_dir),
                                        cpu_only=arguments.cpu_only,
                                        force_gpu_idxs=arguments.force_gpu_idxs
                                        )

    @staticmethod
    def process_faceset_resizer(arguments):
        osex.set_process_lowest_prio()
        from mainscripts import FacesetResizer
        FacesetResizer.process_folder (Path(arguments.input_dir), arguments.image_size, 'same')

    @staticmethod
    def process_dev_test(arguments):
        osex.set_process_lowest_prio()
        from mainscripts import dev_misc
        dev_misc.dev_gen_mask_files(arguments.input_dir)

    @staticmethod
    def process_xsegeditor(arguments):
        osex.set_process_lowest_prio()
        from XSegEditor import XSegEditor
        global exit_code
        exit_code = XSegEditor.start (Path(arguments.input_dir))

    @staticmethod
    def process_xsegapply(arguments):
        osex.set_process_lowest_prio()
        from mainscripts import XSegUtil
        XSegUtil.apply_xseg (Path(arguments.input_dir), Path(arguments.model_dir))

    @staticmethod
    def process_xsegremove(arguments):
        osex.set_process_lowest_prio()
        from mainscripts import XSegUtil
        XSegUtil.remove_xseg (Path(arguments.input_dir))

    @staticmethod
    def process_xsegremovelabels(arguments):
        osex.set_process_lowest_prio()
        from mainscripts import XSegUtil
        XSegUtil.remove_xseg_labels (Path(arguments.input_dir))

    @staticmethod
    def process_xsegfetch(arguments):
        osex.set_process_lowest_prio()
        from mainscripts import XSegUtil
        XSegUtil.fetch_xseg (Path(arguments.input_dir))

    @staticmethod
    def process_extract(config):
        osex.set_process_lowest_prio()
        from mainscripts import Extractor
        Extractor.main(detector=config.detector,
                       input_path=Path(config.input_dir),
                       output_path=Path(config.output_dir),
                       output_debug=config.output_debug,
                       manual_fix=config.manual_fix,
                       manual_output_debug_fix=config.manual_output_debug_fix,
                       manual_window_size=config.manual_window_size,
                       face_type=config.face_type,
                       max_faces_from_image=config.max_faces_from_image,
                       image_size=config.image_size,
                       jpeg_quality=config.jpeg_quality,
                       cpu_only=config.cpu_only,
                       force_gpu_idxs=config.force_gpu_idxs
                       )

    @staticmethod
    def process_sort(config):
        osex.set_process_lowest_prio()
        from mainscripts import Sorter
        Sorter.main(
            input_path=Path(config.input_dir),
            sort_by_method=config.sort_by_method
        )

    @staticmethod
    def process_util(arguments):
        # osex.set_process_lowest_prio()
        from mainscripts import Util

        if arguments.add_landmarks_debug_images:
            Util.add_landmarks_debug_images (input_path=arguments.input_dir)

        if arguments.recover_original_aligned_filename:
            Util.recover_original_aligned_filename (input_path=arguments.input_dir)

        if arguments.save_faceset_metadata:
            Util.save_faceset_metadata_folder (input_path=arguments.input_dir)

        if arguments.restore_faceset_metadata:
            Util.restore_faceset_metadata_folder (input_path=arguments.input_dir)

        if arguments.pack_faceset:
            io.log_info ("Performing faceset packing...\r\n")
            from samplelib import PackedFaceset
            PackedFaceset.pack( Path(arguments.input_dir) )

        if arguments.unpack_faceset:
            io.log_info ("Performing faceset unpacking...\r\n")
            from samplelib import PackedFaceset
            PackedFaceset.unpack( Path(arguments.input_dir) )

        if arguments.export_faceset_mask:
            io.log_info ("Exporting faceset mask..\r\n")
            Util.export_faceset_mask(Path(arguments.input_dir))