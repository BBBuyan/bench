flat_mapping = {
    "properties": {
        "device": {"type": "integer"},
        "number_of_records": {"type": "integer"},
        "activity_sec": {"type": "integer"},
        "total_volume_bytes": {"type": "integer"},
        "subscribers": {"type": "integer"},
        "app": {"type": "keyword"},
        "description": {"type": "text"},
        "info": {"type": "text"}
    }
}

obj1_mapping = {
    "properties": {
        "device": { "type": "integer" },
        "l1": {
            "properties": {
                "device": { "type": "integer" },
                "app": { "type": "keyword" },
                "total_volume_bytes": { "type": "integer" },
                "number_of_records": { "type": "integer" },
                "subscribers": { "type": "integer" },
                "description": {"type": "text"},
                "info": {"type": "text"}
            }
        }
    }
}

obj2_mapping = {
    "properties": {
        "device": { "type": "integer" },
        "l1": {
            "properties": {
                "level": { "type": "integer" },
                "l2": {
                    "properties": {
                        "device": { "type": "integer" },
                        "app": { "type": "keyword" },
                        "total_volume_bytes": { "type": "integer" },
                        "number_of_records": { "type": "integer" },
                        "subscribers": { "type": "integer" },
                        "description": {"type": "text"},
                        "info": {"type": "text"}
                    }
                }
            }
        }
    }
}

obj4_mapping = {
    "properties": {
        "device": { "type": "integer" },
        "l1": {
            "properties": {
                "level": { "type": "integer" },
                "l2": {
                    "properties": {
                        "level": { "type": "integer" },
                        "l3": {
                            "properties": {
                                "level": { "type": "integer" },
                                "l4": {
                                    "properties": {
                                        "device": { "type": "integer" },
                                        "app": { "type": "keyword" },
                                        "total_volume_bytes": { "type": "integer" },
                                        "number_of_records": { "type": "integer" },
                                        "subscribers": { "type": "integer" }
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
        "device": { "type": "integer" },
        "l1": {
            "properties": {
                "level": { "type": "integer" },
                "l2": {
                    "properties": {
                        "level": { "type": "integer" },
                        "l3": {
                            "properties": {
                                "level": { "type": "integer" },
                                "l4": {
                                    "properties": {
                                        "level": { "type": "integer" },
                                        "l5": {
                                            "properties": {
                                                "level": { "type": "integer" },
                                                "l6": {
                                                    "properties": {
                                                        "level": { "type": "integer" },
                                                        "l7": {
                                                            "properties": {
                                                                "level": { "type": "integer" },
                                                                "l8": {
                                                                    "properties": {
                                                                        "device": { "type": "integer" },
                                                                        "app": { "type": "keyword" },
                                                                        "total_volume_bytes": { "type": "integer" },
                                                                        "number_of_records": { "type": "integer" },
                                                                        "subscribers": { "type": "integer" }
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
        "device": {
            "type": "integer"
        },
        "a1": {
            "type": "nested",
            "properties": {
                "device": {"type": "integer"},
                "number_of_records": {"type": "integer"},
                "total_volume_bytes": {"type": "integer"},
                "subscribers": {"type": "integer"},
                "app": {"type": "keyword"},       
                "description": {"type": "text"}, 
                "info": {"type": "text"}        
            }
        }
    }
}

arr2_mapping = {
    "properties": {
        "device": {"type": "integer"},
        "a1": {
            "type": "nested",
            "properties": {
                "level": {"type": "integer"},
                "a2": {
                    "type": "nested",
                    "properties": {
                        "device": {"type": "integer"},
                        "total_volume_bytes": {"type": "integer"},
                        "number_of_records": {"type": "integer"},
                        "subscribers": {"type": "integer"},
                        "app": {"type": "keyword"},
                        "description": {"type": "text"},
                        "info": {"type": "text"}
                    }
                }
            }
        }
    }
}

arr4_mapping = {
    "properties": {
        "device": {"type": "integer"},
        "a1": {
            "type": "nested",
            "properties": {
                "level": {"type": "integer"},
                "a2": {
                    "type": "nested",
                    "properties": {
                        "level": {"type": "integer"},
                        "a3": {
                            "type": "nested",
                            "properties": {
                                "level": {"type": "integer"},
                                "a4": {
                                    "type": "nested",
                                    "properties": {
                                        "device": {"type": "integer"},
                                        "total_volume_bytes": {"type": "integer"},
                                        "number_of_records": {"type": "integer"},
                                        "subscribers": {"type": "integer"},
                                        "app": {"type": "keyword"},
                                        "description": {"type": "text"},
                                        "info": {"type": "text"}
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
        "device": { "type": "integer" },
        "a1": {
            "type": "nested",
            "properties": {
                "level": { "type": "integer" },
                "a2": {
                    "type": "nested",
                    "properties": {
                        "level": { "type": "integer" },
                        "a3": {
                            "type": "nested",
                            "properties": {
                                "level": { "type": "integer" },
                                "a4": {
                                    "type": "nested",
                                    "properties": {
                                        "level": { "type": "integer" },
                                        "a5": {
                                            "type": "nested",
                                            "properties": {
                                                "level": { "type": "integer" },
                                                "a6": {
                                                    "type": "nested",
                                                    "properties": {
                                                        "level": { "type": "integer" },
                                                        "a7": {
                                                            "type": "nested",
                                                            "properties": {
                                                                "level": { "type": "integer" },
                                                                "a8": {
                                                                    "type": "nested",
                                                                    "properties": {
                                                                        "level": { "type": "integer" },
                                                                        "total_volume_bytes": { "type": "integer" },
                                                                        "number_of_records": { "type": "integer" },
                                                                        "subscribers": { "type": "integer" },
                                                                        "app": { "type": "keyword" },
                                                                        "description": {"type": "text"},
                                                                        "info": {"type": "text"}
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

