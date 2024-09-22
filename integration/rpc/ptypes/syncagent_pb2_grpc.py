# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ptypes import syncagent_pb2 as ptypes_dot_syncagent__pb2


class SyncAgentServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FileRemove = channel.unary_unary(
                '/ptypes.SyncAgentService/FileRemove',
                request_serializer=ptypes_dot_syncagent__pb2.FileRemoveRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.FileRename = channel.unary_unary(
                '/ptypes.SyncAgentService/FileRename',
                request_serializer=ptypes_dot_syncagent__pb2.FileRenameRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.FileSend = channel.unary_unary(
                '/ptypes.SyncAgentService/FileSend',
                request_serializer=ptypes_dot_syncagent__pb2.FileSendRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.FilesSync = channel.unary_unary(
                '/ptypes.SyncAgentService/FilesSync',
                request_serializer=ptypes_dot_syncagent__pb2.FilesSyncRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SnapshotClone = channel.unary_unary(
                '/ptypes.SyncAgentService/SnapshotClone',
                request_serializer=ptypes_dot_syncagent__pb2.SnapshotCloneRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.VolumeExport = channel.unary_unary(
                '/ptypes.SyncAgentService/VolumeExport',
                request_serializer=ptypes_dot_syncagent__pb2.VolumeExportRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ReceiverLaunch = channel.unary_unary(
                '/ptypes.SyncAgentService/ReceiverLaunch',
                request_serializer=ptypes_dot_syncagent__pb2.ReceiverLaunchRequest.SerializeToString,
                response_deserializer=ptypes_dot_syncagent__pb2.ReceiverLaunchResponse.FromString,
                )
        self.BackupCreate = channel.unary_unary(
                '/ptypes.SyncAgentService/BackupCreate',
                request_serializer=ptypes_dot_syncagent__pb2.BackupCreateRequest.SerializeToString,
                response_deserializer=ptypes_dot_syncagent__pb2.BackupCreateResponse.FromString,
                )
        self.BackupRemove = channel.unary_unary(
                '/ptypes.SyncAgentService/BackupRemove',
                request_serializer=ptypes_dot_syncagent__pb2.BackupRemoveRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.BackupRestore = channel.unary_unary(
                '/ptypes.SyncAgentService/BackupRestore',
                request_serializer=ptypes_dot_syncagent__pb2.BackupRestoreRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.BackupStatus = channel.unary_unary(
                '/ptypes.SyncAgentService/BackupStatus',
                request_serializer=ptypes_dot_syncagent__pb2.BackupStatusRequest.SerializeToString,
                response_deserializer=ptypes_dot_syncagent__pb2.BackupStatusResponse.FromString,
                )
        self.Reset = channel.unary_unary(
                '/ptypes.SyncAgentService/Reset',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.RestoreStatus = channel.unary_unary(
                '/ptypes.SyncAgentService/RestoreStatus',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=ptypes_dot_syncagent__pb2.RestoreStatusResponse.FromString,
                )
        self.SnapshotPurge = channel.unary_unary(
                '/ptypes.SyncAgentService/SnapshotPurge',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SnapshotPurgeStatus = channel.unary_unary(
                '/ptypes.SyncAgentService/SnapshotPurgeStatus',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=ptypes_dot_syncagent__pb2.SnapshotPurgeStatusResponse.FromString,
                )
        self.ReplicaRebuildStatus = channel.unary_unary(
                '/ptypes.SyncAgentService/ReplicaRebuildStatus',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=ptypes_dot_syncagent__pb2.ReplicaRebuildStatusResponse.FromString,
                )
        self.SnapshotCloneStatus = channel.unary_unary(
                '/ptypes.SyncAgentService/SnapshotCloneStatus',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=ptypes_dot_syncagent__pb2.SnapshotCloneStatusResponse.FromString,
                )
        self.SnapshotHash = channel.unary_unary(
                '/ptypes.SyncAgentService/SnapshotHash',
                request_serializer=ptypes_dot_syncagent__pb2.SnapshotHashRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SnapshotHashStatus = channel.unary_unary(
                '/ptypes.SyncAgentService/SnapshotHashStatus',
                request_serializer=ptypes_dot_syncagent__pb2.SnapshotHashStatusRequest.SerializeToString,
                response_deserializer=ptypes_dot_syncagent__pb2.SnapshotHashStatusResponse.FromString,
                )
        self.SnapshotHashCancel = channel.unary_unary(
                '/ptypes.SyncAgentService/SnapshotHashCancel',
                request_serializer=ptypes_dot_syncagent__pb2.SnapshotHashCancelRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SnapshotHashLockState = channel.unary_unary(
                '/ptypes.SyncAgentService/SnapshotHashLockState',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=ptypes_dot_syncagent__pb2.SnapshotHashLockStateResponse.FromString,
                )


class SyncAgentServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def FileRemove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FileRename(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FileSend(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FilesSync(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SnapshotClone(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VolumeExport(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReceiverLaunch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BackupCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BackupRemove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BackupRestore(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BackupStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Reset(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RestoreStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SnapshotPurge(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SnapshotPurgeStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicaRebuildStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SnapshotCloneStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SnapshotHash(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SnapshotHashStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SnapshotHashCancel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SnapshotHashLockState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SyncAgentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FileRemove': grpc.unary_unary_rpc_method_handler(
                    servicer.FileRemove,
                    request_deserializer=ptypes_dot_syncagent__pb2.FileRemoveRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'FileRename': grpc.unary_unary_rpc_method_handler(
                    servicer.FileRename,
                    request_deserializer=ptypes_dot_syncagent__pb2.FileRenameRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'FileSend': grpc.unary_unary_rpc_method_handler(
                    servicer.FileSend,
                    request_deserializer=ptypes_dot_syncagent__pb2.FileSendRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'FilesSync': grpc.unary_unary_rpc_method_handler(
                    servicer.FilesSync,
                    request_deserializer=ptypes_dot_syncagent__pb2.FilesSyncRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SnapshotClone': grpc.unary_unary_rpc_method_handler(
                    servicer.SnapshotClone,
                    request_deserializer=ptypes_dot_syncagent__pb2.SnapshotCloneRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'VolumeExport': grpc.unary_unary_rpc_method_handler(
                    servicer.VolumeExport,
                    request_deserializer=ptypes_dot_syncagent__pb2.VolumeExportRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ReceiverLaunch': grpc.unary_unary_rpc_method_handler(
                    servicer.ReceiverLaunch,
                    request_deserializer=ptypes_dot_syncagent__pb2.ReceiverLaunchRequest.FromString,
                    response_serializer=ptypes_dot_syncagent__pb2.ReceiverLaunchResponse.SerializeToString,
            ),
            'BackupCreate': grpc.unary_unary_rpc_method_handler(
                    servicer.BackupCreate,
                    request_deserializer=ptypes_dot_syncagent__pb2.BackupCreateRequest.FromString,
                    response_serializer=ptypes_dot_syncagent__pb2.BackupCreateResponse.SerializeToString,
            ),
            'BackupRemove': grpc.unary_unary_rpc_method_handler(
                    servicer.BackupRemove,
                    request_deserializer=ptypes_dot_syncagent__pb2.BackupRemoveRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'BackupRestore': grpc.unary_unary_rpc_method_handler(
                    servicer.BackupRestore,
                    request_deserializer=ptypes_dot_syncagent__pb2.BackupRestoreRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'BackupStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.BackupStatus,
                    request_deserializer=ptypes_dot_syncagent__pb2.BackupStatusRequest.FromString,
                    response_serializer=ptypes_dot_syncagent__pb2.BackupStatusResponse.SerializeToString,
            ),
            'Reset': grpc.unary_unary_rpc_method_handler(
                    servicer.Reset,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'RestoreStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.RestoreStatus,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=ptypes_dot_syncagent__pb2.RestoreStatusResponse.SerializeToString,
            ),
            'SnapshotPurge': grpc.unary_unary_rpc_method_handler(
                    servicer.SnapshotPurge,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SnapshotPurgeStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.SnapshotPurgeStatus,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=ptypes_dot_syncagent__pb2.SnapshotPurgeStatusResponse.SerializeToString,
            ),
            'ReplicaRebuildStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicaRebuildStatus,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=ptypes_dot_syncagent__pb2.ReplicaRebuildStatusResponse.SerializeToString,
            ),
            'SnapshotCloneStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.SnapshotCloneStatus,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=ptypes_dot_syncagent__pb2.SnapshotCloneStatusResponse.SerializeToString,
            ),
            'SnapshotHash': grpc.unary_unary_rpc_method_handler(
                    servicer.SnapshotHash,
                    request_deserializer=ptypes_dot_syncagent__pb2.SnapshotHashRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SnapshotHashStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.SnapshotHashStatus,
                    request_deserializer=ptypes_dot_syncagent__pb2.SnapshotHashStatusRequest.FromString,
                    response_serializer=ptypes_dot_syncagent__pb2.SnapshotHashStatusResponse.SerializeToString,
            ),
            'SnapshotHashCancel': grpc.unary_unary_rpc_method_handler(
                    servicer.SnapshotHashCancel,
                    request_deserializer=ptypes_dot_syncagent__pb2.SnapshotHashCancelRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SnapshotHashLockState': grpc.unary_unary_rpc_method_handler(
                    servicer.SnapshotHashLockState,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=ptypes_dot_syncagent__pb2.SnapshotHashLockStateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ptypes.SyncAgentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SyncAgentService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def FileRemove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.SyncAgentService/FileRemove',
            ptypes_dot_syncagent__pb2.FileRemoveRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FileRename(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.SyncAgentService/FileRename',
            ptypes_dot_syncagent__pb2.FileRenameRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FileSend(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.SyncAgentService/FileSend',
            ptypes_dot_syncagent__pb2.FileSendRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FilesSync(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.SyncAgentService/FilesSync',
            ptypes_dot_syncagent__pb2.FilesSyncRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SnapshotClone(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.SyncAgentService/SnapshotClone',
            ptypes_dot_syncagent__pb2.SnapshotCloneRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VolumeExport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.SyncAgentService/VolumeExport',
            ptypes_dot_syncagent__pb2.VolumeExportRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReceiverLaunch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.SyncAgentService/ReceiverLaunch',
            ptypes_dot_syncagent__pb2.ReceiverLaunchRequest.SerializeToString,
            ptypes_dot_syncagent__pb2.ReceiverLaunchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BackupCreate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.SyncAgentService/BackupCreate',
            ptypes_dot_syncagent__pb2.BackupCreateRequest.SerializeToString,
            ptypes_dot_syncagent__pb2.BackupCreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BackupRemove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.SyncAgentService/BackupRemove',
            ptypes_dot_syncagent__pb2.BackupRemoveRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BackupRestore(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.SyncAgentService/BackupRestore',
            ptypes_dot_syncagent__pb2.BackupRestoreRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BackupStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.SyncAgentService/BackupStatus',
            ptypes_dot_syncagent__pb2.BackupStatusRequest.SerializeToString,
            ptypes_dot_syncagent__pb2.BackupStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Reset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.SyncAgentService/Reset',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RestoreStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.SyncAgentService/RestoreStatus',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ptypes_dot_syncagent__pb2.RestoreStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SnapshotPurge(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.SyncAgentService/SnapshotPurge',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SnapshotPurgeStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.SyncAgentService/SnapshotPurgeStatus',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ptypes_dot_syncagent__pb2.SnapshotPurgeStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplicaRebuildStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.SyncAgentService/ReplicaRebuildStatus',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ptypes_dot_syncagent__pb2.ReplicaRebuildStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SnapshotCloneStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.SyncAgentService/SnapshotCloneStatus',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ptypes_dot_syncagent__pb2.SnapshotCloneStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SnapshotHash(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.SyncAgentService/SnapshotHash',
            ptypes_dot_syncagent__pb2.SnapshotHashRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SnapshotHashStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.SyncAgentService/SnapshotHashStatus',
            ptypes_dot_syncagent__pb2.SnapshotHashStatusRequest.SerializeToString,
            ptypes_dot_syncagent__pb2.SnapshotHashStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SnapshotHashCancel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.SyncAgentService/SnapshotHashCancel',
            ptypes_dot_syncagent__pb2.SnapshotHashCancelRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SnapshotHashLockState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ptypes.SyncAgentService/SnapshotHashLockState',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ptypes_dot_syncagent__pb2.SnapshotHashLockStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)