import attr
from datetime import datetime

@attr.s
class Torrent:   
    added_on = attr.ib(converter=datetime.fromtimestamp, default=None)  # 1567622307
    amount_left = attr.ib(default=None)  # 0
    auto_tmm = attr.ib(default=None)  # False
    category = attr.ib(default=None)  # 
    completed = attr.ib(default=None)  # 739136165
    completion_on = attr.ib(converter=datetime.fromtimestamp, default=None)  # 1567622388
    dl_limit = attr.ib(default=None)  # -1
    dlspeed = attr.ib(default=None)  # 0
    downloaded = attr.ib(default=None)  # 744254714
    downloaded_session = attr.ib(default=None)  # 0
    eta = attr.ib(default=None)  # 8640000
    f_l_piece_prio = attr.ib(default=None)  # False
    force_start = attr.ib(default=None)  # False
    hash = attr.ib(default=None)  # f0554d264c6ffa2606deb1f0389b223efa40fc57
    last_activity = attr.ib(converter=datetime.fromtimestamp, default=None)  # 1568360483
    magnet_uri = attr.ib(default=None)  # magnet:?xt=urn:btih:f0554d264c6ffa2606deb1f0389b223efa40fc57&dn=%5bHorribleSubs%5d%20Black%20Clover%20-%2099%20%5b720p%5d.mkv&tr=http%3a%2f%2fnyaa.tracker.wf%3a7777%2fannounce&tr=udp%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.internetwarriors.net%3a1337%2fannounce&tr=udp%3a%2f%2ftracker.leechersparadise.org%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2fopen.stealth.si%3a80%2fannounce&tr=udp%3a%2f%2fp4p.arenabg.com%3a1337%2fannounce&tr=udp%3a%2f%2fmgtracker.org%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.tiny-vps.com%3a6969%2fannounce&tr=udp%3a%2f%2fpeerfect.org%3a6969%2fannounce&tr=http%3a%2f%2fshare.camoe.cn%3a8080%2fannounce&tr=http%3a%2f%2ft.nyaatracker.com%3a80%2fannounce&tr=https%3a%2f%2fopen.kickasstracker.com%3a443%2fannounce
    max_ratio = attr.ib(default=None)  # -1
    max_seeding_time = attr.ib(default=None)  # -1
    name = attr.ib(default=None)  # [HorribleSubs] Black Clover - 99 [720p].mkv
    num_complete = attr.ib(default=None)  # 814
    num_incomplete = attr.ib(default=None)  # 42
    num_leechs = attr.ib(default=None)  # 0
    num_seeds = attr.ib(default=None)  # 0
    priority = attr.ib(default=None)  # 0
    progress = attr.ib(default=None)  # 1
    ratio = attr.ib(default=None)  # 0.28732304005265596
    ratio_limit = attr.ib(default=None)  # -2
    save_path = attr.ib(default=None)  # E:\Torrent Downloads\raw\
    seeding_time_limit = attr.ib(default=None)  # -2
    seen_complete = attr.ib(default=None)  # 4294967295
    seq_dl = attr.ib(default=None)  # False
    size = attr.ib(default=None)  # 739136165
    state = attr.ib(default=None)  # queuedUP
    super_seeding = attr.ib(default=None)  # False
    tags = attr.ib(default=None)  # 
    time_active = attr.ib(default=None)  # 12115
    total_size = attr.ib(default=None)  # 739136165
    tracker = attr.ib(default=None)  # http://nyaa.tracker.wf:7777/announce
    up_limit = attr.ib(default=None)  # -1
    uploaded = attr.ib(default=None)  # 213841527
    uploaded_session = attr.ib(default=None)  # 0
    upspeed = attr.ib(default=None)  # 0
