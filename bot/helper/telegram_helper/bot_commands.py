from bot import CMD_INDEX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f'start{CMD_INDEX}'
        self.MirrorCommand = f'mega_mirror{CMD_INDEX}'
        self.UnzipMirrorCommand = f'extract{CMD_INDEX}'
        self.ZipMirrorCommand = f'zip{CMD_INDEX}'
        self.CancelMirror = f'cancel{CMD_INDEX}'
        self.CancelAllCommand = f'cancelall{CMD_INDEX}'
        self.ListCommand = f'find{CMD_INDEX}'
        self.SearchCommand = f'search{CMD_INDEX}'
        self.StatusCommand = f'status{CMD_INDEX}'
        self.AuthorizedUsersCommand = f'users{CMD_INDEX}'
        self.AuthorizeCommand = f'authorize{CMD_INDEX}'
        self.UnAuthorizeCommand = f'unauthorize{CMD_INDEX}'
        self.AddSudoCommand = f'addsudo{CMD_INDEX}'
        self.RmSudoCommand = f'rmsudo{CMD_INDEX}'
        self.PingCommand = f'ping{CMD_INDEX}'
        self.RestartCommand = f'restart{CMD_INDEX}'
        self.StatsCommand = f'stats{CMD_INDEX}'
        self.HelpCommand = f'help{CMD_INDEX}'
        self.LogCommand = f'log{CMD_INDEX}'
        self.CloneCommand = f'clone{CMD_INDEX}'
        self.CountCommand = f'count{CMD_INDEX}'
        self.WatchCommand = f'yt_mirror{CMD_INDEX}'
        self.ZipWatchCommand = f'yt_zip_mirror{CMD_INDEX}'
        self.QbMirrorCommand = f'qb_mirror{CMD_INDEX}'
        self.QbUnzipMirrorCommand = f'qb_unzip_pmirror{CMD_INDEX}'
        self.QbZipMirrorCommand = f'qb_zip_pmirror{CMD_INDEX}'
        self.DeleteCommand = f'del{CMD_INDEX}'
        self.ShellCommand = f'shell{CMD_INDEX}'
        self.ExecHelpCommand = f'exechelp{CMD_INDEX}'
        self.LeechSetCommand = f'settings{CMD_INDEX}'
        self.SetThumbCommand = f'savethumbnail{CMD_INDEX}'
        self.LeechCommand = f'mega_leech{CMD_INDEX}'
        self.UnzipLeechCommand = f'extract_leech{CMD_INDEX}'
        self.ZipLeechCommand = f'zip_leech{CMD_INDEX}'
        self.QbLeechCommand = f'qb_leech{CMD_INDEX}'
        self.QbUnzipLeechCommand = f'qb_extract_leech{CMD_INDEX}'
        self.QbZipLeechCommand = f'qb_zip_leech{CMD_INDEX}'
        self.LeechWatchCommand = f'yt_leech{CMD_INDEX}'
        self.LeechZipWatchCommand = f'yt_zip_leech{CMD_INDEX}'
        self.RssListCommand = f'rsslist{CMD_INDEX}'
        self.RssGetCommand = f'rssget{CMD_INDEX}'
        self.RssSubCommand = f'rsssub{CMD_INDEX}'
        self.RssUnSubCommand = f'rssunsub{CMD_INDEX}'
        self.RssSettingsCommand = f'rssset{CMD_INDEX}'
        self.EvalCommand = f'eval{CMD_INDEX}'
        self.ExecCommand = f'exec{CMD_INDEX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_INDEX}'

BotCommands = _BotCommands()
