#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as r
from modules.webidl.HTMLElement import HTMLElement

class HTMLMediaElement(HTMLElement):
    '''
    The HTMLMediaElement interface adds to HTMLElement the properties and methods needed to
    support basic media-related capabilities that are common to audio and video.
    The HTMLVideoElement and HTMLAudioElement elements both inherit this interface.
    '''
    # properties
    # This interface also inherits properties from its ancestors HTMLElement, Element, Node, and EventTarget.

    def p_audioTracks(self):
        # TODO：想办法对该返回对象的属性进行Fuzz测试
        # 返回 AudioTrackList对象 表示音视频的可用音轨
        # 任何主流浏览器都不支持 audioTracks 属性
        '''
        1.AudioTrackList对象表示音视频的可用音轨。
        AudioTrackList 对象：
        audioTracks.length - 或者可用音轨的数量
        audioTracks.getTrackById(id) - 通过 id 来获得 AudioTrack 对象
        audioTracks[index] - 通过 index 来获得 AudioTrack 对象
        注释：首个可用的 AudioTrack 对象的下标是 0。
        2.AudioTrack 对象表示音轨。
        AudioTrack 对象的属性：
        id - 获得音轨的 id
        kind - 获得音轨的类型（可以是 "alternative", "description", "main", "translation", "commentary", 或者 "" （空字符串））
        label - 获得音轨的标签
        language - 获得音轨的语言
        enabled - 获得或设置音轨是否是活动的 (true|false)
        '''
        pass

    def p_autoplay(self):
        # 设置或返回是否在就绪（加载完成）后随即播放音频
        return r.bool()

    def p_autostart(self):
        # 设置或返回是否在就绪（加载完成）后随即播放音频
        return r.bool()

    def p_buffered(self):
        # 返回表示音频已缓冲部分的 TimeRanges 对象
        pass

    def p_controller(self):
        # 返回表示音频当前媒体控制器的 MediaController 对象
        pass

    def p_controls(self):
        # 设置或返回音频是否应该显示控件（比如播放/暂停等）
        return r.bool()

    def p_crossOrigin(self):
        # 设置或返回音频的 CORS 设置
        # TODO:什么是Cross设置搞清楚
        return r.DOMString(r.zint(256))

    def p_currentSrc(self):
        pass

    def p_currentTime(self):
        # 当前播放的时间，单位秒
        return r.double(24*60*60)

    def p_defaultMuted(self):
        # 设置或返回音频默认是否静音
        return r.bool()

    def p_defaultPlaybackRate(self):
        # 设置或返回音频的默认播放速度
        return r.choice([2.0, 1.0, 0.5, 0, -0.5, -1.0, ])

    def p_disableRemotePlayback(self):
        # A Boolean that sets or returns the remote playback state,
        # indicating whether the media element is allowed to have a remote playback UI.
        return r.bool()

    def p_duration(self):
        # 返回当前音频的长度（以秒计）
        pass

    def p_ended(self):
        # 返回音频的播放是否已结束
        pass

    def p_error(self):
        # 返回表示音频错误状态的 MediaError 对象
        pass

    def p_initialTime(self):
        pass

    def p_loop(self):
        # 设置或返回音频是否应在结束时重新播放
        return r.bool()

    def p_mediaGroup(self):
        # 设置或返回音频所属的组合（用于连接多个音频元素）
        # TODO:这个值的范围暂且不确定
        return r.DOMString(r.zint(256))

    def p_mediaKeys(self):
        pass

    #def p_mozAudioCaptured(self):
    #    pass

    #def p_mozAudioChannelType(self):
    #    return r.DOMString(r.zint(256))

    #def p_mozChannels(self):
    #    pass

    #def p_mozFragmentEnd(self):
    #    return r.double()

    #def p_mozFrameBufferLength(self):
    #    return randoms.unsigendlong()

    #def p_mozSampleRate(self):
    #    pass

    def p_muted(self):
        # 设置或返回音频是否静音
        return r.bool()

    def p_networkState(self):
        # 返回音频的当前网络状态
        pass

    def p_paused(self):
        # 设置或返回音频是否暂停
        return r.bool()

    def p_playbackRate(self):
        # 设置或返回音频播放的速度
        return r.choice([2.0, 1.0, 0.5, 0, -0.5, -1.0, ])

    def p_played(self):
        # 返回表示音频已播放部分的 TimeRanges 对象
        pass

    def p_preload(self):
        # 设置或返回音频是否应该在页面加载后进行加载
        return r.choice(["auto", "metadata", "null"])

    def p_preservesPitch(self):
        return r.bool()

    def p_readyState(self):
        # 返回音频当前的就绪状态
        pass

    def p_seekable(self):
        # 返回表示音频可寻址部分的 TimeRanges 对象
        pass

    def p_seeking(self):
        # 返回用户是否正在音频中进行查找
        pass

    def p_sinkId(self):
        pass

    def p_src(self):
        # 设置或返回音频元素的当前来源
        # TODO:添加真正的音频样本
        return r.DOMString(r.zint(256))

    def p_srcObject(self):
        # TODO set
        pass

    def p_textTracks(self):
        # 返回表示可用文本轨道的 TextTrackList 对象
        pass

    def p_videoTracks(self):
        pass

    def p_volume(self):
        # 设置或返回音频的音量
        return r.double(1)

    # Event handler properties
    def p_onmozinterruptbegin(self):
        return r.Funcs()

    def p_onmozinterruptend(self):
        return r.Funcs()

    def p_onencrypted(self):
        return r.Funcs()

    # Methods
    # This interface also inherits methods from its ancestors HTMLElement, Element, Node, and EventTarget.
    def m_addTextTrack(self):
        # 在音频中添加一个新的文本轨道
        pass

    def m_canPlayType(self):
        # 检查浏览器是否可以播放指定的音频类型
        return "'%s'" % r.MIMEType()

    def m_fastSeek(self):
        # 在音频播放器中指定播放时间
        return r.double(24*60*60)

    def m_getStartDate(self):
        # 返回一个新的Date对象，表示当前时间轴偏移量
        pass

    def m_load(self):
        # 重新加载音频元素
        pass

    #def m_mozCaptureStream(self):
    #    pass

    #def m_mozCaptureStreamUntilEnded(self):
    #    pass

    #def m_mozGetMetadata(self):
    #    pass

    #def m_mozLoadFrom(self):
    #    pass

    def m_pause(self):
        # 暂停当前播放的音频
        pass

    def m_play(self):
        # 开始播放音频
        pass

    #def m_setMediaKeys(self):
    #    pass

    def m_setSinkId(self):
        # TODO:需要优化
        return "'%s'" % r.DOMString(r.zint(256))
