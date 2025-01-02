SDCP_FILE_TRANSFER_ACK = [
    None,
    "Not currently transferring files",
    "Already in file verification phase",
    "File not found",
]

SDCP_FROM = ["PC via LAN", "PC via WAN", "Web Client", "App", "Server"]


SDCP_MACHINE_STATUS = [
    "Idle",
    "Printing",
    "File Transferring",
    "Exposure Testing",
    "Devices Testing",
]

SDCP_PRINT_STATUS = [
    "Idle",
    "Homing",
    "Descending",
    "Exposing",
    "Lifting",
    "Pausing",
    "Paused",
    "Stopping",
    "Stopped",
    "Complete",
    "File Checking",
]

SDCP_PRINT_ERROR = [
    None,
    "MD5 Check Failed",
    "File Read Failed",
    "Resolution Mismatch",
    "Format Mismatch",
    "Machine Model Mismatch",
]

SDCP_ERROR_CODE = [None, "File Transfer MD5 Check Failed", "File Format is Incorrect"]

SDCP_STORAGE_TYPE = ["Internal Storage", "External Storage"]

SDCP_STORAGE_ITEM_TYPE = ["Folder", "File"]

SDCP_TASK_STATUS = ["Other", "Completed", "Exception", "Stopped"]

SDCP_TIME_LAPSE_VIDEO = [
    "Not shot",
    "File exists",
    "Deleted",
    "Generating",
    "Generation Failed",
]

SDCP_PRINT_CAUSE = [
    None,
    "Over-temperature",
    "Strain Gauge Calibration Failed",
    "Resin Level Low",
    "Model Requires More Resin than Max Vat Capacity",
    "No Resin Detected",
    "Foreign Object Detected",
    "Auto-leveling Failed",
    "Model Detachment Detected",
    "Strain Gauge Not Detected",
    "LCD Screen Connection Abnormal",
    "Cumulative Release Film Usage Reached Max Use",
    "USB Drive Removed - Print Stopped",
    "X-axis Motor Anomaly - Print Stopped",
    "Z-azis Motor Anomaly - Print Stopped",
    "Resin Level too High - Print Stopped",
    "Resin Level too Low - Print Stopped",
    "Home Position Calibration Failed",
    "Model Detected On Platform",
    "Error",
    "Motor Movement Abnormal",
    "No Model Detected",
    "Warping of Model Detected",
    "Home Y-axis Home Position Calidation Failed",
    "File Error",
    "Camera Error",
    "Network Error",
    "Server Connection Failed",
    "Disconnected from App",
    "Check Install and Data Cable Connection of Automatic Material Extraction / Feed Machine",
    "Resin Level Low",
    "Check Install and Data Cable Connection of Automatic Material Extraction / Feed Machine",
    "Automatic Material Extraction Timed Out",
    "Resin Vat Temperature Sensor Disconnected",
    "Resin Vat Over-temperature",
]
