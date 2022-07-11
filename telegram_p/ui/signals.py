from PySide6.QtCore import QObject,Signal


class StatusupdatedSignal(QObject):
    status_updated = Signal(dict, str)
    status_updated_proxy = Signal(dict, str)
    status_updated_message = Signal(dict, str)
    status_updated_all = Signal(str, int, str)
class NotifProxy(QObject):
    Notif_stt_proxy = Signal(str,int)


class NotifSignals(QObject):
    Notif_updated = Signal(str, int, str)
    Notif_stt = Signal(str)

class GetmemSignals(QObject):
    get_mem_updated = Signal(list)
    get_mem__nolink = Signal(str)
    get_admin = Signal(list)

class ADDmemSignals(QObject):
    add_mem_updated_from_acc = Signal(str, int, str)
    add_mem_updated_from_user = Signal(str, int, str)
    chatkickban_updated_from_user = Signal(str, int, str)
    chatmesspam_updated_from_user = Signal(str, int, str)
    add_data_from_user = Signal(str)
    stt_success = Signal()
    stt_fail = Signal()




class Connect_all_Signals(NotifSignals,StatusupdatedSignal,GetmemSignals,ADDmemSignals,NotifProxy):
    pass

    # taint_agent_status = Signal(
    #     str,
    #     name='taintAgentStatus',
    #     arguments=['IP address or hostname']
    # )

    # agent_gone_online = Signal(
    #     str,
    #     name='agentGoneOnline',
    #     arguments=['Hostname or IP Address']
    # )

    # agent_gone_offline = Signal(
    #     str,
    #     name='agentGoneOffline',
    #     arguments=['Hostname or IP Address']
    # )

    # agent_status_changed = Signal(
    #     str, str, str,
    #     name='agentStatusChanged',
    #     arguments=['Hostname or IP Address', 'Previous Status', 'New Status']
    # )

    # agent_failed = Signal(
    #     str,
    #     name='agentFailed',
    #     arguments=['Hostname or IP Address']
    # )

    # primary_candidate_add = Signal(
    #     str,
    #     name='primaryCandidateAdd',
    #     arguments=['host']
    # )

    # primary_candidate_remove = Signal(
    #     str,
    #     name='primaryCandidateRemove',
    #     arguments=['host']
    # )

    # agents_changed = Signal(
    #     name='agentsChanged',
    #     arguments=['host']
    # )


# class RegistrySignals(QObject):
#     registry_updated = Signal(
#         name='registryUpdated'
#     )

#     taint_agent_status = Signal(
#         str,
#         name='taintAgentStatus',
#         arguments=['IP address or hostname']
#     )


class RegistryModelSignals(QObject):
    agent_selected_status_changed = Signal(
        str, bool,
        name='agentSelectedStatusChanged',
        arguments=['IP address or hostname', 'selected']
    )


class MainUISignals(QObject):
    agent_manually_added = Signal(
        str,
        name='agentManuallyAdded',
        arguments=['IP address or hostname']
    )

    agent_manually_removed = Signal(
        str, str,
        name='agentManuallyRemoved',
        arguments=['IP address or hostname', 'Agent UUID']
    )

    agent_custom_settings_updated = Signal(
        str, dict,
        name='agentCustomSettingsUpdated',
        arguments=['IP address or hostname',
                   'Dictionary of updated custom settings']
    )


class ZeroConfSignals(QObject):
    zeroconf_agent_found = Signal(
        str, str, str, str,
        name='zeroconfAgentFound',
        arguments=['zeroconf name', 'ip address', 'port', 'uuid']
    )

    zeroconf_agent_removed = Signal(
        str,
        name='zeroconfAgentRemoved',
        arguments=['zeroconf name']
    )


class ParkingCacheUpdaterSignals(QObject):
    # signals that the cache is ready
    # if the list has items in it, those need to be loaded into the database
    #
    # [
    #     [index, type, name, number, airlineCodes],
    #     # e.g.
    #     [20, "gate", "Gate 20", "", "QFA"]
    # ]
    #
    #
    # n.b. name is passed to fgfs, e.g. `--parkpos="Gate 20"`
    #
    parking_cache_ready = Signal(
        str, list,
        name='parkingCacheReady',
        arguments=['airport code', 'records']
    )