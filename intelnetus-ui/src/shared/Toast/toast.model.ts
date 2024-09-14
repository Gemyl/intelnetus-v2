export enum MessageType {
    SUCCESS = "success",
    ERROR = "error",
    INFO = "info",
    WARNING = "warning"
}

export interface Toast {
    header?: string;
    body: string;
    type: string;
    icon?: string;
    delay?: number;
}