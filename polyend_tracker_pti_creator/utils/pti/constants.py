# pylint: disable=too-many-lines
# adapted from https://github.com/jaap3/pti-file-format/blob/main/pti.rst

PLAYBACK_VALUES = {
    'one-shot': 0,
    'forward-loop': 1,
    'backward-loop': 2,
    'ping-pong-loop': 3,
    'slice': 4,
    'beat-slice': 5,
    'wavetable': 6,
    'granular': 7
}

PTI_HEADER_DEFINITION = {
    'file_type_indicator': {
        'description': 'File type indicator',
        'type': '2s',
        'value': b'TI',
    },
    'unknown_01': {
        'description': 'unknown - 1',
        'type': 'B',
        'value': 1,
    },
    'unknown_02': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_03': {
        'description': 'unknown - 1',
        'type': 'B',
        'value': 1,
    },
    'unknown_04': {
        'description': 'unknown - 2, 4, 5',
        'type': 'B',
        'value': 4,
    },
    'unknown_05': {
        'description': 'unknown - 0, 1, 2',
        'type': 'B',
        'value': 1,
    },
    'unknown_06': {
        'description': 'unknown - 1',
        'type': 'B',
        'value': 1,
    },
    'unknown_07': {
        'description': 'unknown - 6, 9',
        'type': 'B',
        'value': 9,
    },
    'unknown_08': {
        'description': 'unknown - 6, 9',
        'type': 'B',
        'value': 9,
    },
    'unknown_09': {
        'description': 'unknown - 6, 9',
        'type': 'B',
        'value': 9,
    },
    'unknown_10': {
        'description': 'unknown - 6, 9',
        'type': 'B',
        'value': 9,
    },
    'unknown_11': {
        'description': 'unknown - 116',
        'type': 'B',
        'value': 116,
    },
    'unknown_12': {
        'description': 'unknown - 1',
        'type': 'B',
        'value': 1,
    },
    'unknown_13': {
        'description': 'unknown - 0, 102, 110',
        'type': 'B',
        'value': 110,
    },
    'unknown_14': {
        'description': 'unknown - 0, 102',
        'type': 'B',
        'value': 102,
    },
    'unknown_15': {
        'description': 'unknown - 1',
        'type': 'B',
        'value': 1,
    },
    'unknown_16': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_17': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_18': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'is_wavetable': {
        'description': 'Is set to 1 (True) when Sample playback is set to Wavetable',
        'type': '?',
        'value': False,
    },
    'instrument_name': {
        'description': 'ASCII characters',
        'type': '32s',
        'value': b''.join([b'\x00' for x in range(32)]),
    },
    'unknown_19': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_20': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_21': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_22': {
        'description': 'unknown - ?',
        'type': 'B',
        'value': 184,
    },
    'unknown_23': {
        'description': 'unknown - ?',
        'type': 'B',
        'value': 110,
    },
    'unknown_24': {
        'description': 'unknown - ?',
        'type': 'B',
        'value': 2,
    },
    'unknown_25': {
        'description': 'unknown - ?',
        'type': 'B',
        'value': 112,
    },
    'sample_length': {
        'description': 'long: 0-4294967295',
        'type': 'L',
        'value': 0,
    },
    'wavetable_window_size': {
        'description': 'short: 32, 64, 128, 256, 1024, 2048',
        'type': 'H',
        'value': 2048,
    },
    'unknown_26': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_27': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'wavetable_total_positions': {
        'description': 'short: 0-65535',
        'type': 'H',
        'value': 0,
    },
    'unknown_28': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_29': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_30': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_31': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_32': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_33': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'sample_playback': {
        'description': '0: 1-Shot (default) '
                       '1: Forward loop '
                       '2: Backward loop '
                       '3: PingPong loop '
                       '4: Slice '
                       '5: Beat slice '
                       '6: Wavetable '
                       '7: Granular',
        'type': 'B',
        'value': 0,
    },
    'unknown_34': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'playback_start': {
        'description': 'short: 0-65535',
        'type': 'H',
        'value': 0,
    },
    'loop_start': {
        'description': 'short: 1-65534',
        'type': 'H',
        'value': 1,
    },
    'loop_end': {
        'description': 'short: 1-65534',
        'type': 'H',
        'value': 65534,
    },
    'playback_end': {
        'description': 'short: 0-65535',
        'type': 'H',
        'value': 65535,
    },
    'unknown_35': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_36': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'wavetable_position': {
        'description': 'short: 0-65535',
        'type': 'H',
        'value': 0,
    },
    'unknown_37': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_38': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    # Volume Automation Envelope
    'volume_env_amount': {
        'description': 'float: 0.0 - 1.0 (0-100%)',
        'type': 'f',
        'value': 1.0,
    },
    'unknown_39': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_40': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'volume_env_attack': {
        'description': 'short: 0-10000 (0-10 seconds)',
        'type': 'H',
        'value': 0,
    },
    'unknown_41': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_42': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'volume_env_decay': {
        'description': 'short: 0-10000 (0-10 seconds)',
        'type': 'H',
        'value': 0,
    },
    'volume_env_sustain': {
        'description': 'float: 0.0 - 1.0 (0-100%)',
        'type': 'f',
        'value': 1.0,
    },
    'volume_env_release': {
        'description': 'short: 0-10000 (0-10 seconds)',
        'type': 'H',
        'value': 1000,
    },
    'volume_automation_type_1': {
        'description': '00: Off '
                       '01: Envelope (default) '
                       '11: LFO',
        'type': 'B',
        'value': 0,
    },
    'volume_automation_type_2': {
        'description': '00: Off '
                       '01: Envelope (default) '
                       '11: LFO',
        'type': 'B',
        'value': 1,
    },
    # Panning Automation Envelope
    'panning_env_amount': {
        'description': 'float: 0.0 - 1.0 (0-100%)',
        'type': 'f',
        'value': 1.0,
    },
    'unknown_43': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_44': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'panning_env_attack': {
        'description': 'short: 0-10000 (0-10 seconds)',
        'type': 'H',
        'value': 0,
    },
    'unknown_45': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_46': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'panning_env_decay': {
        'description': 'short: 0-10000 (0-10 seconds)',
        'type': 'H',
        'value': 0,
    },
    'panning_env_sustain': {
        'description': 'float: 0.0 - 1.0 (0-100%)',
        'type': 'f',
        'value': 1.0,
    },
    'panning_env_release': {
        'description': 'short: 0-10000 (0-10 seconds)',
        'type': 'H',
        'value': 1000,
    },
    'panning_automation_type_1': {
        'description': '00: Off '
                       '01: Envelope (default) '
                       '11: LFO',
        'type': 'B',
        'value': 0,
    },
    'panning_automation_type_2': {
        'description': '00: Off '
                       '01: Envelope (default) '
                       '11: LFO',
        'type': 'B',
        'value': 0,
    },
    # Cutoff Automation Envelope
    'cutoff_env_amount': {
        'description': 'float: 0.0 - 1.0 (0-100%)',
        'type': 'f',
        'value': 1.0,
    },
    'unknown_47': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_48': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'cutoff_env_attack': {
        'description': 'short: 0-10000 (0-10 seconds)',
        'type': 'H',
        'value': 0,
    },
    'unknown_49': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_50': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'cutoff_env_decay': {
        'description': 'short: 0-10000 (0-10 seconds)',
        'type': 'H',
        'value': 0,
    },
    'cutoff_env_sustain': {
        'description': 'float: 0.0 - 1.0 (0-100%)',
        'type': 'f',
        'value': 1.0,
    },
    'cutoff_env_release': {
        'description': 'short: 0-10000 (0-10 seconds)',
        'type': 'H',
        'value': 1000,
    },
    'cutoff_automation_type_1': {
        'description': '00: Off '
                       '01: Envelope (default) '
                       '11: LFO',
        'type': 'B',
        'value': 0,
    },
    'cutoff_automation_type_2': {
        'description': '00: Off '
                       '01: Envelope (default) '
                       '11: LFO',
        'type': 'B',
        'value': 0,
    },
    # Wavetable Position Automation Envelope
    'wt_pos_env_amount': {
        'description': 'float: 0.0 - 1.0 (0-100%)',
        'type': 'f',
        'value': 1.0,
    },
    'unknown_51': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_52': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'wt_pos_env_attack': {
        'description': 'short: 0-10000 (0-10 seconds)',
        'type': 'H',
        'value': 0,
    },
    'unknown_53': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_54': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'wt_pos_env_decay': {
        'description': 'short: 0-10000 (0-10 seconds)',
        'type': 'H',
        'value': 0,
    },
    'wt_pos_env_sustain': {
        'description': 'float: 0.0 - 1.0 (0-100%)',
        'type': 'f',
        'value': 1.0,
    },
    'wt_pos_env_release': {
        'description': 'short: 0-10000 (0-10 seconds)',
        'type': 'H',
        'value': 1000,
    },
    'wt_pos_automation_type_1': {
        'description': '00: Off '
                       '01: Envelope (default) '
                       '11: LFO',
        'type': 'B',
        'value': 0,
    },
    'wt_pos_automation_type_2': {
        'description': '00: Off '
                       '01: Envelope (default) '
                       '11: LFO',
        'type': 'B',
        'value': 0,
    },
    # Granular Position Automation Envelope
    'gran_pos_env_amount': {
        'description': 'float: 0.0 - 1.0 (0-100%)',
        'type': 'f',
        'value': 1.0,
    },
    'unknown_55': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_56': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'gran_pos_env_attack': {
        'description': 'short: 0-10000 (0-10 seconds)',
        'type': 'H',
        'value': 0,
    },
    'unknown_57': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_58': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'gran_pos_env_decay': {
        'description': 'short: 0-10000 (0-10 seconds)',
        'type': 'H',
        'value': 0,
    },
    'gran_pos_env_sustain': {
        'description': 'float: 0.0 - 1.0 (0-100%)',
        'type': 'f',
        'value': 1.0,
    },
    'gran_pos_env_release': {
        'description': 'short: 0-10000 (0-10 seconds)',
        'type': 'H',
        'value': 1000,
    },
    'gran_pos_automation_type_1': {
        'description': '00: Off '
                       '01: Envelope (default) '
                       '11: LFO',
        'type': 'B',
        'value': 0,
    },
    'gran_pos_automation_type_2': {
        'description': '00: Off '
                       '01: Envelope (default) '
                       '11: LFO',
        'type': 'B',
        'value': 0,
    },
    # Finetune Automation Envelope
    'finetune_env_amount': {
        'description': 'float: 0.0 - 1.0 (0-100%)',
        'type': 'f',
        'value': 1.0,
    },
    'unknown_59': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_60': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'finetune_env_attack': {
        'description': 'short: 0-10000 (0-10 seconds)',
        'type': 'H',
        'value': 0,
    },
    'unknown_61': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_62': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'finetune_env_decay': {
        'description': 'short: 0-10000 (0-10 seconds)',
        'type': 'H',
        'value': 0,
    },
    'finetune_env_sustain': {
        'description': 'float: 0.0 - 1.0 (0-100%)',
        'type': 'f',
        'value': 1.0,
    },
    'finetune_env_release': {
        'description': 'short: 0-10000 (0-10 seconds)',
        'type': 'H',
        'value': 1000,
    },
    'finetune_automation_type_1': {
        'description': '00: Off '
                       '01: Envelope (default) '
                       '11: LFO',
        'type': 'B',
        'value': 0,
    },
    'finetune_automation_type_2': {
        'description': '00: Off '
                       '01: Envelope (default) '
                       '11: LFO',
        'type': 'B',
        'value': 0,
    },
    # Volume Automation LFO
    'volume_auto_lfo_type': {
        'description': '0: Rev Saw '
                       '1: Saw '
                       '2: Triangle (default) '
                       '3: Square '
                       '4: Random',
        'type': 'B',
        'value': 2,
    },
    'volume_auto_lfo_steps': {
        'description': '0: 24 steps (default) '
                       '1: 16 steps '
                       '2: 12 steps '
                       '3: 8 steps '
                       '4: 6 steps '
                       '5: 4 steps '
                       '6: 3 steps '
                       '7: 2 steps '
                       '8: 3/2 step '
                       '9: 1 step '
                       '10: 3/4 step '
                       '11: 1/2 step '
                       '12: 3/8 step '
                       '13: 1/3 step '
                       '14: 1/4 step '
                       '15: 3/16 step '
                       '16: 1/6 step '
                       '17: 1/8 step '
                       '18: 1/12 step '
                       '19: 1/16 step '
                       '20: 1/24 step '
                       '21: 1/32 step '
                       '22: 1/48 step '
                       '23: 1/64 step',
        'type': 'B',
        'value': 0,
    },
    'unknown_63': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_64': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'volume_auto_lfo_amount': {
        'description': 'float: 0.0 - 1.0 (0-100%)',
        'type': 'f',
        'value': 0.5,
    },
    # Panning Automation LFO
    'panning_auto_lfo_type': {
        'description': '0: Rev Saw '
                       '1: Saw '
                       '2: Triangle (default) '
                       '3: Square '
                       '4: Random',
        'type': 'B',
        'value': 2,
    },
    'panning_auto_lfo_steps': {
        'description': '0: 24 steps (default) '
                       '1: 16 steps '
                       '2: 12 steps '
                       '3: 8 steps '
                       '4: 6 steps '
                       '5: 4 steps '
                       '6: 3 steps '
                       '7: 2 steps '
                       '8: 3/2 step '
                       '9: 1 step '
                       '10: 3/4 step '
                       '11: 1/2 step '
                       '12: 3/8 step '
                       '13: 1/3 step '
                       '14: 1/4 step '
                       '15: 3/16 step '
                       '16: 1/6 step '
                       '17: 1/8 step '
                       '18: 1/12 step '
                       '19: 1/16 step '
                       '20: 1/24 step '
                       '21: 1/32 step '
                       '22: 1/48 step '
                       '23: 1/64 step',
        'type': 'B',
        'value': 0,
    },
    'unknown_65': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_66': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'panning_auto_lfo_amount': {
        'description': 'float: 0.0 - 1.0 (0-100%)',
        'type': 'f',
        'value': 0.5,
    },
    # Cutoff Automation LFO
    'cutoff_auto_lfo_type': {
        'description': '0: Rev Saw '
                       '1: Saw '
                       '2: Triangle (default) '
                       '3: Square '
                       '4: Random',
        'type': 'B',
        'value': 2,
    },
    'cutoff_auto_lfo_steps': {
        'description': '0: 24 steps (default) '
                       '1: 16 steps '
                       '2: 12 steps '
                       '3: 8 steps '
                       '4: 6 steps '
                       '5: 4 steps '
                       '6: 3 steps '
                       '7: 2 steps '
                       '8: 3/2 step '
                       '9: 1 step '
                       '10: 3/4 step '
                       '11: 1/2 step '
                       '12: 3/8 step '
                       '13: 1/3 step '
                       '14: 1/4 step '
                       '15: 3/16 step '
                       '16: 1/6 step '
                       '17: 1/8 step '
                       '18: 1/12 step '
                       '19: 1/16 step '
                       '20: 1/24 step '
                       '21: 1/32 step '
                       '22: 1/48 step '
                       '23: 1/64 step',
        'type': 'B',
        'value': 0,
    },
    'unknown_67': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_68': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'cutoff_auto_lfo_amount': {
        'description': 'float: 0.0 - 1.0 (0-100%)',
        'type': 'f',
        'value': 0.5,
    },
    # Wavetable Position Automation LFO
    'wt_pos_auto_lfo_type': {
        'description': '0: Rev Saw '
                       '1: Saw '
                       '2: Triangle (default) '
                       '3: Square '
                       '4: Random',
        'type': 'B',
        'value': 2,
    },
    'wt_pos_auto_lfo_steps': {
        'description': '0: 24 steps (default) '
                       '1: 16 steps '
                       '2: 12 steps '
                       '3: 8 steps '
                       '4: 6 steps '
                       '5: 4 steps '
                       '6: 3 steps '
                       '7: 2 steps '
                       '8: 3/2 step '
                       '9: 1 step '
                       '10: 3/4 step '
                       '11: 1/2 step '
                       '12: 3/8 step '
                       '13: 1/3 step '
                       '14: 1/4 step '
                       '15: 3/16 step '
                       '16: 1/6 step '
                       '17: 1/8 step '
                       '18: 1/12 step '
                       '19: 1/16 step '
                       '20: 1/24 step '
                       '21: 1/32 step '
                       '22: 1/48 step '
                       '23: 1/64 step',
        'type': 'B',
        'value': 0,
    },
    'unknown_69': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_70': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'wt_pos_auto_lfo_amount': {
        'description': 'float: 0.0 - 1.0 (0-100%)',
        'type': 'f',
        'value': 0.5,
    },
    # Granular Position Automation LFO
    'gran_pos_auto_lfo_type': {
        'description': '0: Rev Saw '
                       '1: Saw '
                       '2: Triangle (default) '
                       '3: Square '
                       '4: Random',
        'type': 'B',
        'value': 2,
    },
    'gran_pos_auto_lfo_steps': {
        'description': '0: 24 steps (default) '
                       '1: 16 steps '
                       '2: 12 steps '
                       '3: 8 steps '
                       '4: 6 steps '
                       '5: 4 steps '
                       '6: 3 steps '
                       '7: 2 steps '
                       '8: 3/2 step '
                       '9: 1 step '
                       '10: 3/4 step '
                       '11: 1/2 step '
                       '12: 3/8 step '
                       '13: 1/3 step '
                       '14: 1/4 step '
                       '15: 3/16 step '
                       '16: 1/6 step '
                       '17: 1/8 step '
                       '18: 1/12 step '
                       '19: 1/16 step '
                       '20: 1/24 step '
                       '21: 1/32 step '
                       '22: 1/48 step '
                       '23: 1/64 step',
        'type': 'B',
        'value': 0,
    },
    'unknown_71': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_72': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'gran_pos_auto_lfo_amount': {
        'description': 'float: 0.0 - 1.0 (0-100%)',
        'type': 'f',
        'value': 0.5,
    },
    # Finetune Automation LFO
    'finetune_auto_lfo_type': {
        'description': '0: Rev Saw '
                       '1: Saw '
                       '2: Triangle (default) '
                       '3: Square '
                       '4: Random',
        'type': 'B',
        'value': 2,
    },
    'finetune_auto_lfo_steps': {
        'description': '0: 24 steps (default) '
                       '1: 16 steps '
                       '2: 12 steps '
                       '3: 8 steps '
                       '4: 6 steps '
                       '5: 4 steps '
                       '6: 3 steps '
                       '7: 2 steps '
                       '8: 3/2 step '
                       '9: 1 step '
                       '10: 3/4 step '
                       '11: 1/2 step '
                       '12: 3/8 step '
                       '13: 1/3 step '
                       '14: 1/4 step '
                       '15: 3/16 step '
                       '16: 1/6 step '
                       '17: 1/8 step '
                       '18: 1/12 step '
                       '19: 1/16 step '
                       '20: 1/24 step '
                       '21: 1/32 step '
                       '22: 1/48 step '
                       '23: 1/64 step',
        'type': 'B',
        'value': 0,
    },
    'unknown_73': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_74': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'finetune_auto_lfo_amount': {
        'description': 'float: 0.0 - 1.0 (0-100%)',
        'type': 'f',
        'value': 0.5,
    },
    # Filter
    'cutoff': {
        'description': 'float: 0.0 - 1.0 (0-100%)',
        'type': 'f',
        'value': 1.0,
    },
    'resonance': {
        'description': 'float: 0.0 - 4.300000190734863 (0-100%)',
        'type': 'f',
        'value': 0.0,
    },
    'filter_type_1': {
        'description': '00: Disabled (default) '
                       '01: Low-pass '
                       '11: High-pass '
                       '21: Band-pass',
        'type': 'B',
        'value': 0,
    },
    'filter_type_2': {
        'description': '00: Disabled (default) '
                       '01: Low-pass '
                       '11: High-pass '
                       '21: Band-pass',
        'type': 'B',
        'value': 0,
    },
    # Instrument parameters / effects
    'tune': {
        'description': 'signed char: -/+24',
        'type': 'b',
        'value': 0,
    },
    'finetune': {
        'description': 'signed char: -/+100',
        'type': 'b',
        'value': 0,
    },
    'volume': {
        'description': '0: -inf dB '
                       '1-100: -/+24 dB',
        'type': 'B',
        'value': 50,
    },
    'unknown_75': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_76': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_77': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'panning': {
        'description': '0-100: -/+50',
        'type': 'B',
        'value': 50,
    },
    'unknown_78': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'delay_send': {
        'description': '0: -inf dB '
                       '1-100: -39.6/+0 dB',
        'type': 'B',
        'value': 0,
    },
    'unknown_79': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    # Slices
    'slice_01_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_02_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_03_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_04_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_05_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_06_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_07_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_08_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_09_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_10_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_11_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_12_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_13_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_14_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_15_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_16_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_17_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_18_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_19_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_20_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_21_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_22_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_23_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_24_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_25_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_26_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_27_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_28_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_29_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_30_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_31_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_32_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_33_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_34_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_35_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_36_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_37_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_38_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_39_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_40_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_41_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_42_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_43_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_44_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_45_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_46_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_47_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'slice_48_adjust': {
        'description': 'short: 0-65535 '
                       'Calculate the offset using (value / 65535) * (sample length in ms) '
                       "Value range is limited by the preceeding slice's adjust value",
        'type': 'H',
        'value': 0,
    },
    'number_of_slices': {
        'description': '0-48',
        'type': 'B',
        'value': 0,
    },
    'active_slice': {
        'description': '0-47',
        'type': 'B',
        'value': 0,
    },
    # Granular
    'granular_length': {
        'description': 'Short: 44-44100 (1.0 - 1000.0 ms)',
        'type': 'H',
        'value': 441,
    },
    'granular_position': {
        'description': 'Short: 0-65535 (start-end)',
        'type': 'H',
        'value': 0,
    },
    'granular_shape': {
        'description': '0: Square (default) '
                       '1: Triangle '
                       '2: Gauss',
        'type': 'B',
        'value': 0,
    },
    'granular_loop_mode': {
        'description': '0: Forward (default) '
                       '1: Backward '
                       '2: PingPong',
        'type': 'B',
        'value': 0,
    },
    # More Effects
    'reverb_send': {
        'description': '0: -inf dB '
                       '1-100: -39.6/+0 dB',
        'type': 'B',
        'value': 0,
    },
    'overdrive': {
        'description': '0-100: 0-100%',
        'type': 'B',
        'value': 0,
    },
    'bit_depth': {
        'description': '4-16: 4-16 bit',
        'type': 'B',
        'value': 16,
    },
    'unknown_80': {
        'description': 'unknown - 0',
        'type': 'B',
        'value': 0,
    },
    'unknown_81': {
        'description': 'unknown - ?',
        'type': 'B',
        'value': 171,
    },
    'unknown_82': {
        'description': 'unknown - ?',
        'type': 'B',
        'value': 44,
    },
    'unknown_83': {
        'description': 'unknown - ?',
        'type': 'B',
        'value': 201,
    },
    'unknown_84': {
        'description': 'unknown - ?',
        'type': 'B',
        'value': 240,
    },
}
