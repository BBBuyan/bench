flat_mapping = {
    "properties": {
        "memory_usage_mb": {"type": "integer"},
        "error_count": {"type": "integer"},
        "total_storage": {"type": "integer"},
        "temp": {"type": "integer"},
        "uptime_hours": {"type": "integer"},
        "app": {"type": "keyword"},
        "description": {"type": "text"},
        "info": {"type": "text"}
    }
}

obj1_mapping = {
    "properties": {
        "memory_usage_mb": { "type": "integer" },
        "l1": {
            "properties": {
                "memory_usage_mb": { "type": "integer" },
                "error_count": { "type": "integer" },
                "total_storage_gb": { "type": "integer" },
                "temp": { "type": "integer" },
                "uptime_hours": {"type": "integer"},
                "app": { "type": "keyword" },
                "info": {"type": "text"},
                "description": {"type": "text"},
            }
        }
    }
}

obj2_mapping = {
    "properties": {
        "memory_usage_mb": { "type": "integer" },
        "l1": {
            "properties": {
                "memory_usage_mb": { "type": "integer" },
                "l2": {
                    "properties": {
                        "memory_usage_mb": { "type": "integer" },
                        "error_count": { "type": "integer" },
                        "total_storage_gb": { "type": "integer" },
                        "temp": { "type": "integer" },
                        "uptime_hours": {"type": "integer"},
                        "app": { "type": "keyword" },
                        "info": {"type": "text"},
                        "description": {"type": "text"},
                    }
                }
            }
        }
    }
}

obj4_mapping = {
    "properties": {
        "memory_usage_mb": { "type": "integer" },
        "l1": {
            "properties": {
                "memory_usage_mb": { "type": "integer" },
                "l2": {
                    "properties": {
                        "memory_usage_mb": { "type": "integer" },
                        "l3": {
                            "properties": {
                                "memory_usage_mb": { "type": "integer" },
                                "l4": {
                                    "properties": {
                                        "memory_usage_mb": { "type": "integer" },
                                        "error_count": { "type": "integer" },
                                        "total_storage_gb": { "type": "integer" },
                                        "temp": { "type": "integer" },
                                        "uptime_hours": {"type": "integer"},
                                        "app": { "type": "keyword" },
                                        "info": {"type": "text"},
                                        "description": {"type": "text"},
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
obj8_mapping= {
    "properties": {
        "memory_usage_mb": { "type": "integer" },
        "l1": {
            "properties": {
                "memory_usage_mb": { "type": "integer" },
                "l2": {
                    "properties": {
                        "memory_usage_mb": { "type": "integer" },
                        "l3": {
                            "properties": {
                                "memory_usage_mb": { "type": "integer" },
                                "l4": {
                                    "properties": {
                                        "memory_usage_mb": { "type": "integer" },
                                        "l5": {
                                            "properties": {
                                                "memory_usage_mb": { "type": "integer" },
                                                "l6": {
                                                    "properties": {
                                                        "memory_usage_mb": { "type": "integer" },
                                                        "l7": {
                                                            "properties": {
                                                                "memory_usage_mb": { "type": "integer" },
                                                                "l8": {
                                                                    "properties": {
                                                                        "memory_usage_mb": { "type": "integer" },
                                                                        "error_count": { "type": "integer" },
                                                                        "total_storage_gb": { "type": "integer" },
                                                                        "temp": { "type": "integer" },
                                                                        "uptime_hours": {"type": "integer"},
                                                                        "app": { "type": "keyword" },
                                                                        "info": {"type": "text"},
                                                                        "description": {"type": "text"},
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

arr1_mapping = {
    "properties": {
        "memory_usage_mb": {
            "type": "integer"
        },
        "a1": {
            "type": "nested",
            "properties": {
                "memory_usage_mb": { "type": "integer" },
                "error_count": { "type": "integer" },
                "total_storage_gb": { "type": "integer" },
                "temp": { "type": "integer" },
                "uptime_hours": {"type": "integer"},
                "app": { "type": "keyword" },
                "info": {"type": "text"},
                "description": {"type": "text"},
            }
        }
    }
}

arr2_mapping = {
    "properties": {
        "memory_usage_mb": {"type": "integer"},
        "a1": {
            "type": "nested",
            "properties": {
                "memory_usage_mb": {"type": "integer"},
                "a2": {
                    "type": "nested",
                    "properties": {
                        "memory_usage_mb": { "type": "integer" },
                        "error_count": { "type": "integer" },
                        "total_storage_gb": { "type": "integer" },
                        "temp": { "type": "integer" },
                        "uptime_hours": {"type": "integer"},
                        "app": { "type": "keyword" },
                        "info": {"type": "text"},
                        "description": {"type": "text"},
                    }
                }
            }
        }
    }
}

arr4_mapping = {
    "properties": {
        "memory_usage_mb": {"type": "integer"},
        "a1": {
            "type": "nested",
            "properties": {
                "memory_usage_mb": {"type": "integer"},
                "a2": {
                    "type": "nested",
                    "properties": {
                        "memory_usage_mb": {"type": "integer"},
                        "a3": {
                            "type": "nested",
                            "properties": {
                                "memory_usage_mb": {"type": "integer"},
                                "a4": {
                                    "type": "nested",
                                    "properties": {
                                        "memory_usage_mb": { "type": "integer" },
                                        "error_count": { "type": "integer" },
                                        "total_storage_gb": { "type": "integer" },
                                        "temp": { "type": "integer" },
                                        "uptime_hours": {"type": "integer"},
                                        "app": { "type": "keyword" },
                                        "info": {"type": "text"},
                                        "description": {"type": "text"},
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

arr8_mapping = {
    "properties": {
        "memory_usage_mb": { "type": "integer" },
        "a1": {
            "type": "nested",
            "properties": {
                "memory_usage_mb": { "type": "integer" },
                "a2": {
                    "type": "nested",
                    "properties": {
                        "memory_usage_mb": { "type": "integer" },
                        "a3": {
                            "type": "nested",
                            "properties": {
                                "memory_usage_mb": { "type": "integer" },
                                "a4": {
                                    "type": "nested",
                                    "properties": {
                                        "memory_usage_mb": { "type": "integer" },
                                        "a5": {
                                            "type": "nested",
                                            "properties": {
                                                "memory_usage_mb": { "type": "integer" },
                                                "a6": {
                                                    "type": "nested",
                                                    "properties": {
                                                        "memory_usage_mb": { "type": "integer" },
                                                        "a7": {
                                                            "type": "nested",
                                                            "properties": {
                                                                "memory_usage_mb": { "type": "integer" },
                                                                "a8": {
                                                                    "type": "nested",
                                                                    "properties": {
                                                                        "memory_usage_mb": { "type": "integer" },
                                                                        "error_count": { "type": "integer" },
                                                                        "total_storage_gb": { "type": "integer" },
                                                                        "temp": { "type": "integer" },
                                                                        "uptime_hours": {"type": "integer"},
                                                                        "app": { "type": "keyword" },
                                                                        "info": {"type": "text"},
                                                                        "description": {"type": "text"},
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

