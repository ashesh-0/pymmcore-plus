from typing import Protocol, runtime_checkable

from pymmcore_plus.core.events._protocol import PSignal


@runtime_checkable
class PMDASignaler(Protocol):
    """Declares the protocol for all signals that will be emitted from [`pymmcore_plus.mda.MDARunner`][]."""  # noqa: E501

    sequenceStarted: PSignal
    """Emits `(sequence: MDASequence, metadata: dict)` when an acquisition sequence is started."""  # noqa: E501
    sequencePauseToggled: PSignal
    """Emits `(paused: bool)` when an acquisition sequence is paused or unpaused."""
    sequenceCanceled: PSignal
    """Emits `(sequence: MDASequence)` when an acquisition sequence is canceled."""
    sequenceFinished: PSignal
    """Emits `(sequence: MDASequence)` when an acquisition sequence is finished."""
    frameReady: PSignal
    """Emits `(img: np.ndarray, event: MDAEvent, metadata: dict)` after an image is acquired during an acquisition sequence."""  # noqa: E501
