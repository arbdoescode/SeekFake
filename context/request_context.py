import contextvars

request_id_var = contextvars.ContextVar("request_id", default=None)
user_id_var = contextvars.ContextVar("user_id", default=None)