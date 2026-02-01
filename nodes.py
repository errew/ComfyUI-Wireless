"""
ComfyUI Wireless Data Nodes
Standard: PEP 8
Features: Singleton storage, Type-safe variants (Any, Image, Latent).
"""

import logging
from typing import Any, Dict, Tuple, Optional

# Setup Logger
logger = logging.getLogger("ComfyUI.Wireless")

# Global Singleton Storage
_GLOBAL_CONTEXT: Dict[str, Any] = {}


class GlobalStore:
    """
    Singleton class to manage global variable storage safely.
    """
    
    @staticmethod
    def set(key: str, value: Any) -> None:
        """Sets a value in the global context."""
        if not key:
            logger.warning("GlobalStore: Attempted to set a variable with an empty key.")
            return
        
        # Strip whitespace to prevent "video_vae " != "video_vae" errors
        cleaned_key = key.strip()
        if cleaned_key != key:
             logger.info(f"GlobalStore: Warning - Key has leading/trailing whitespace. Auto-fixing '{key}' -> '{cleaned_key}'")
        
        _GLOBAL_CONTEXT[cleaned_key] = value

    @staticmethod
    def get(key: str) -> Any:
        """Retrieves a value from the global context."""
        if not key:
            raise ValueError("GlobalStore: Key cannot be empty.")
            
        # Strip whitespace to match how it is stored
        cleaned_key = key.strip()
            
        if cleaned_key not in _GLOBAL_CONTEXT:
            # Raise a clear error instead of returning None to prevent downstream "NoneType" crashes.
            # We list available keys to help the user debug typos.
            available_keys = list(_GLOBAL_CONTEXT.keys())
            raise ValueError(f"Wireless Error: Key '{cleaned_key}' not found. (Input was '{key}').\n"
                             f"Available keys: {available_keys}\n"
                             f"Please ensure the 'Set Wireless' node executes BEFORE this 'Get Wireless' node.")
            
        return _GLOBAL_CONTEXT[cleaned_key]


class BaseSetNode:
    """Base class for all Set nodes to share logic."""
    FUNCTION = "execute"
    CATEGORY = "Wireless"
    OUTPUT_NODE = True

    def execute(self, key: str, value: Any) -> Tuple[Any]:
        GlobalStore.set(key, value)
        return (value,)


class BaseGetNode:
    """Base class for all Get nodes to share logic."""
    FUNCTION = "execute"
    CATEGORY = "Wireless"

    def execute(self, key: str) -> Tuple[Any]:
        val = GlobalStore.get(key)
        return (val,)


# --- 1. Universal (Any) Nodes ---

class SetNodeAny(BaseSetNode):
    """Sets a global variable of any type."""
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        return {
            "required": {
                "key": ("STRING", {"default": "var_name", "multiline": False}),
                "value": ("*", {}), 
            }
        }
    
    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("value",)


class GetNodeAny(BaseGetNode):
    """Gets a global variable of any type."""
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        return {
            "required": {
                "key": ("STRING", {"default": "var_name", "multiline": False}),
            }
        }
    
    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("value",)


# --- 2. Image Nodes ---

class SetNodeImage(BaseSetNode):
    """Sets a global variable strictly for Images."""
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        return {
            "required": {
                "key": ("STRING", {"default": "img_var", "multiline": False}),
                "image": ("IMAGE", {}), 
            }
        }
    
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)

    def execute(self, key: str, image: Any) -> Tuple[Any]:
        return super().execute(key, image)


class GetNodeImage(BaseGetNode):
    """Gets a global variable strictly for Images."""
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        return {
            "required": {
                "key": ("STRING", {"default": "img_var", "multiline": False}),
            }
        }
    
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)


# --- 3. Latent Nodes ---

class SetNodeLatent(BaseSetNode):
    """Sets a global variable strictly for Latents."""
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        return {
            "required": {
                "key": ("STRING", {"default": "latent_var", "multiline": False}),
                "latent": ("LATENT", {}), 
            }
        }
    
    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("latent",)

    def execute(self, key: str, latent: Any) -> Tuple[Any]:
        return super().execute(key, latent)


class GetNodeLatent(BaseGetNode):
    """Gets a global variable strictly for Latents."""
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        return {
            "required": {
                "key": ("STRING", {"default": "latent_var", "multiline": False}),
            }
        }
    
    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("latent",)


# --- Registration ---

NODE_CLASS_MAPPINGS = {
    "WirelessSetAny": SetNodeAny,
    "WirelessGetAny": GetNodeAny,
    "WirelessSetImage": SetNodeImage,
    "WirelessGetImage": GetNodeImage,
    "WirelessSetLatent": SetNodeLatent,
    "WirelessGetLatent": GetNodeLatent,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WirelessSetAny": "Set Wireless (Any)",
    "WirelessGetAny": "Get Wireless (Any)",
    "WirelessSetImage": "Set Wireless (Image)",
    "WirelessGetImage": "Get Wireless (Image)",
    "WirelessSetLatent": "Set Wireless (Latent)",
    "WirelessGetLatent": "Get Wireless (Latent)",
}
