# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 12:57:57 2016

@author: Parag Guruji, paragguruji@gmail.com
"""


mapping = {
    "mappings" : {
      "tweet" : {
        "properties" : {
          "coordinates" : {
            "properties" : {
              "coordinates" : {
                "type" : "double"
              },
              "type" : {
                "type" : "string"
              }
            }
          },
          "created_at" : {
            "type" : "date",
            "format" : "E MMM d H:m:s z Y"
          },
          "entities" : {
            "properties" : {
              "hashtags" : {
                "properties" : {
                  "indices" : {
                    "type" : "long"
                  },
                  "text" : {
                    "type" : "string"
                  }
                }
              },
              "symbols" : {
                "properties" : {
                  "indices" : {
                    "type" : "long"
                  },
                  "text" : {
                    "type" : "string"
                  }
                }
              },
              "urls" : {
                "properties" : {
                  "display_url" : {
                    "type" : "string"
                  },
                  "expanded_url" : {
                    "type" : "string"
                  },
                  "indices" : {
                    "type" : "long"
                  },
                  "url" : {
                    "type" : "string"
                  }
                }
              },
              "user_mentions" : {
                "properties" : {
                  "id" : {
                    "type" : "long"
                  },
                  "id_str" : {
                    "type" : "string"
                  },
                  "indices" : {
                    "type" : "long"
                  },
                  "name" : {
                    "type" : "string"
                  },
                  "screen_name" : {
                    "type" : "string"
                  }
                }
              }
            }
          },
          "favorite_count" : {
            "type" : "long"
          },
          "favorited" : {
            "type" : "boolean"
          },
          "geo" : {
            "properties" : {
              "coordinates" : {
                "type" : "double"
              },
              "type" : {
                "type" : "string"
              }
            }
          },
          "id" : {
            "type" : "long"
          },
          "id_str" : {
            "type" : "string"
          },
          "in_reply_to_screen_name" : {
            "type" : "string"
          },
          "in_reply_to_status_id" : {
            "type" : "long"
          },
          "in_reply_to_status_id_str" : {
            "type" : "string"
          },
          "in_reply_to_user_id" : {
            "type" : "long"
          },
          "in_reply_to_user_id_str" : {
            "type" : "string"
          },
          "is_quote_status" : {
            "type" : "boolean"
          },
          "lang" : {
            "type" : "string"
          },
          "outdated" : {
            "type" : "string"
          },
          "place" : {
            "properties" : {
              "attributes" : {
                "type" : "object"
              },
              "bounding_box" : {
                "properties" : {
                  "coordinates" : {
                    "type" : "double"
                  },
                  "type" : {
                    "type" : "string"
                  }
                }
              },
              "country" : {
                "type" : "string"
              },
              "country_code" : {
                "type" : "string"
              },
              "full_name" : {
                "type" : "string"
              },
              "id" : {
                "type" : "string"
              },
              "name" : {
                "type" : "string"
              },
              "place_type" : {
                "type" : "string"
              },
              "url" : {
                "type" : "string"
              }
            }
          },
          "possibly_sensitive" : {
            "type" : "boolean"
          },
          "quoted_status" : {
            "properties" : {
              "coordinates" : {
                "properties" : {
                  "coordinates" : {
                    "type" : "double"
                  },
                  "type" : {
                    "type" : "string"
                  }
                }
              },
              "created_at" : {
                "type" : "string"
              },
              "entities" : {
                "properties" : {
                  "hashtags" : {
                    "properties" : {
                      "indices" : {
                        "type" : "long"
                      },
                      "text" : {
                        "type" : "string"
                      }
                    }
                  },
                  "symbols" : {
                    "properties" : {
                      "indices" : {
                        "type" : "long"
                      },
                      "text" : {
                        "type" : "string"
                      }
                    }
                  },
                  "urls" : {
                    "properties" : {
                      "display_url" : {
                        "type" : "string"
                      },
                      "expanded_url" : {
                        "type" : "string"
                      },
                      "indices" : {
                        "type" : "long"
                      },
                      "url" : {
                        "type" : "string"
                      }
                    }
                  },
                  "user_mentions" : {
                    "properties" : {
                      "id" : {
                        "type" : "long"
                      },
                      "id_str" : {
                        "type" : "string"
                      },
                      "indices" : {
                        "type" : "long"
                      },
                      "name" : {
                        "type" : "string"
                      },
                      "screen_name" : {
                        "type" : "string"
                      }
                    }
                  }
                }
              },
              "extended_entities" : {
                "type" : "object"
              },
              "favorite_count" : {
                "type" : "long"
              },
              "favorited" : {
                "type" : "boolean"
              },
              "geo" : {
                "properties" : {
                  "coordinates" : {
                    "type" : "double"
                  },
                  "type" : {
                    "type" : "string"
                  }
                }
              },
              "id" : {
                "type" : "long"
              },
              "id_str" : {
                "type" : "string"
              },
              "in_reply_to_screen_name" : {
                "type" : "string"
              },
              "in_reply_to_status_id" : {
                "type" : "long"
              },
              "in_reply_to_status_id_str" : {
                "type" : "string"
              },
              "in_reply_to_user_id" : {
                "type" : "long"
              },
              "in_reply_to_user_id_str" : {
                "type" : "string"
              },
              "is_quote_status" : {
                "type" : "boolean"
              },
              "lang" : {
                "type" : "string"
              },
              "place" : {
                "properties" : {
                  "attributes" : {
                    "type" : "object"
                  },
                  "bounding_box" : {
                    "properties" : {
                      "coordinates" : {
                        "type" : "double"
                      },
                      "type" : {
                        "type" : "string"
                      }
                    }
                  },
                  "country" : {
                    "type" : "string"
                  },
                  "country_code" : {
                    "type" : "string"
                  },
                  "full_name" : {
                    "type" : "string"
                  },
                  "id" : {
                    "type" : "string"
                  },
                  "name" : {
                    "type" : "string"
                  },
                  "place_type" : {
                    "type" : "string"
                  },
                  "url" : {
                    "type" : "string"
                  }
                }
              },
              "possibly_sensitive" : {
                "type" : "boolean"
              },
              "quoted_status_id" : {
                "type" : "long"
              },
              "quoted_status_id_str" : {
                "type" : "string"
              },
              "retweet_count" : {
                "type" : "long"
              },
              "retweeted" : {
                "type" : "boolean"
              },
              "scopes" : {
                "properties" : {
                  "followers" : {
                    "type" : "boolean"
                  }
                }
              },
              "source" : {
                "type" : "string"
              },
              "text" : {
                "type" : "string"
              },
              "truncated" : {
                "type" : "boolean"
              },
              "user" : {
                "properties" : {
                  "id" : {
                    "type" : "long"
                  },
                  "id_str" : {
                    "type" : "string"
                  }
                }
              }
            }
          },
          "quoted_status_id" : {
            "type" : "long"
          },
          "quoted_status_id_str" : {
            "type" : "string"
          },
          "retweet_count" : {
            "type" : "long"
          },
          "retweeted" : {
            "type" : "boolean"
          },
          "retweeted_status" : {
            "properties" : {
              "coordinates" : {
                "properties" : {
                  "coordinates" : {
                    "type" : "double"
                  },
                  "type" : {
                    "type" : "string"
                  }
                }
              },
              "created_at" : {
                "type" : "string"
              },
              "entities" : {
                "properties" : {
                  "hashtags" : {
                    "properties" : {
                      "indices" : {
                        "type" : "long"
                      },
                      "text" : {
                        "type" : "string"
                      }
                    }
                  },
                  "symbols" : {
                    "properties" : {
                      "indices" : {
                        "type" : "long"
                      },
                      "text" : {
                        "type" : "string"
                      }
                    }
                  },
                  "urls" : {
                    "properties" : {
                      "display_url" : {
                        "type" : "string"
                      },
                      "expanded_url" : {
                        "type" : "string"
                      },
                      "indices" : {
                        "type" : "long"
                      },
                      "url" : {
                        "type" : "string"
                      }
                    }
                  },
                  "user_mentions" : {
                    "properties" : {
                      "id" : {
                        "type" : "long"
                      },
                      "id_str" : {
                        "type" : "string"
                      },
                      "indices" : {
                        "type" : "long"
                      },
                      "name" : {
                        "type" : "string"
                      },
                      "screen_name" : {
                        "type" : "string"
                      }
                    }
                  }
                }
              },
              "extended_entities" : {
                "type" : "object"
              },
              "favorite_count" : {
                "type" : "long"
              },
              "favorited" : {
                "type" : "boolean"
              },
              "geo" : {
                "properties" : {
                  "coordinates" : {
                    "type" : "double"
                  },
                  "type" : {
                    "type" : "string"
                  }
                }
              },
              "id" : {
                "type" : "long"
              },
              "id_str" : {
                "type" : "string"
              },
              "in_reply_to_screen_name" : {
                "type" : "string"
              },
              "in_reply_to_status_id" : {
                "type" : "long"
              },
              "in_reply_to_status_id_str" : {
                "type" : "string"
              },
              "in_reply_to_user_id" : {
                "type" : "long"
              },
              "in_reply_to_user_id_str" : {
                "type" : "string"
              },
              "is_quote_status" : {
                "type" : "boolean"
              },
              "lang" : {
                "type" : "string"
              },
              "place" : {
                "properties" : {
                  "attributes" : {
                    "type" : "object"
                  },
                  "bounding_box" : {
                    "properties" : {
                      "coordinates" : {
                        "type" : "double"
                      },
                      "type" : {
                        "type" : "string"
                      }
                    }
                  },
                  "country" : {
                    "type" : "string"
                  },
                  "country_code" : {
                    "type" : "string"
                  },
                  "full_name" : {
                    "type" : "string"
                  },
                  "id" : {
                    "type" : "string"
                  },
                  "name" : {
                    "type" : "string"
                  },
                  "place_type" : {
                    "type" : "string"
                  },
                  "url" : {
                    "type" : "string"
                  }
                }
              },
              "possibly_sensitive" : {
                "type" : "boolean"
              },
              "quoted_status" : {
                "properties" : {
                  "coordinates" : {
                    "properties" : {
                      "coordinates" : {
                        "type" : "double"
                      },
                      "type" : {
                        "type" : "string"
                      }
                    }
                  },
                  "created_at" : {
                    "type" : "string"
                  },
                  "entities" : {
                    "properties" : {
                      "hashtags" : {
                        "properties" : {
                          "indices" : {
                            "type" : "long"
                          },
                          "text" : {
                            "type" : "string"
                          }
                        }
                      },
                      "urls" : {
                        "properties" : {
                          "display_url" : {
                            "type" : "string"
                          },
                          "expanded_url" : {
                            "type" : "string"
                          },
                          "indices" : {
                            "type" : "long"
                          },
                          "url" : {
                            "type" : "string"
                          }
                        }
                      },
                      "user_mentions" : {
                        "properties" : {
                          "id" : {
                            "type" : "long"
                          },
                          "id_str" : {
                            "type" : "string"
                          },
                          "indices" : {
                            "type" : "long"
                          },
                          "name" : {
                            "type" : "string"
                          },
                          "screen_name" : {
                            "type" : "string"
                          }
                        }
                      }
                    }
                  },
                  "extended_entities" : {
                    "type" : "object"
                  },
                  "favorite_count" : {
                    "type" : "long"
                  },
                  "favorited" : {
                    "type" : "boolean"
                  },
                  "geo" : {
                    "properties" : {
                      "coordinates" : {
                        "type" : "double"
                      },
                      "type" : {
                        "type" : "string"
                      }
                    }
                  },
                  "id" : {
                    "type" : "long"
                  },
                  "id_str" : {
                    "type" : "string"
                  },
                  "in_reply_to_screen_name" : {
                    "type" : "string"
                  },
                  "in_reply_to_status_id" : {
                    "type" : "long"
                  },
                  "in_reply_to_status_id_str" : {
                    "type" : "string"
                  },
                  "in_reply_to_user_id" : {
                    "type" : "long"
                  },
                  "in_reply_to_user_id_str" : {
                    "type" : "string"
                  },
                  "is_quote_status" : {
                    "type" : "boolean"
                  },
                  "lang" : {
                    "type" : "string"
                  },
                  "place" : {
                    "properties" : {
                      "attributes" : {
                        "type" : "object"
                      },
                      "bounding_box" : {
                        "properties" : {
                          "coordinates" : {
                            "type" : "double"
                          },
                          "type" : {
                            "type" : "string"
                          }
                        }
                      },
                      "country" : {
                        "type" : "string"
                      },
                      "country_code" : {
                        "type" : "string"
                      },
                      "full_name" : {
                        "type" : "string"
                      },
                      "id" : {
                        "type" : "string"
                      },
                      "name" : {
                        "type" : "string"
                      },
                      "place_type" : {
                        "type" : "string"
                      },
                      "url" : {
                        "type" : "string"
                      }
                    }
                  },
                  "possibly_sensitive" : {
                    "type" : "boolean"
                  },
                  "quoted_status_id" : {
                    "type" : "long"
                  },
                  "quoted_status_id_str" : {
                    "type" : "string"
                  },
                  "retweet_count" : {
                    "type" : "long"
                  },
                  "retweeted" : {
                    "type" : "boolean"
                  },
                  "scopes" : {
                    "properties" : {
                      "place_ids" : {
                        "type" : "string"
                      }
                    }
                  },
                  "source" : {
                    "type" : "string"
                  },
                  "text" : {
                    "type" : "string"
                  },
                  "truncated" : {
                    "type" : "boolean"
                  },
                  "user" : {
                    "properties" : {
                      "id" : {
                        "type" : "long"
                      },
                      "id_str" : {
                        "type" : "string"
                      }
                    }
                  }
                }
              },
              "quoted_status_id" : {
                "type" : "long"
              },
              "quoted_status_id_str" : {
                "type" : "string"
              },
              "retweet_count" : {
                "type" : "long"
              },
              "retweeted" : {
                "type" : "boolean"
              },
              "scopes" : {
                "properties" : {
                  "followers" : {
                    "type" : "boolean"
                  },
                  "place_ids" : {
                    "type" : "string"
                  }
                }
              },
              "source" : {
                "type" : "string"
              },
              "text" : {
                "type" : "string"
              },
              "truncated" : {
                "type" : "boolean"
              },
              "user" : {
                "properties" : {
                  "id" : {
                    "type" : "long"
                  },
                  "id_str" : {
                    "type" : "string"
                  }
                }
              }
            }
          },
          "saved_at" : {
            "type" : "date",
            "format" : "E MMM d H:m:s z Y"
          },
          "source" : {
            "type" : "string"
          },
          "text" : {
            "type" : "string"
          },
          "truncated" : {
            "type" : "boolean"
          },
          "user" : {
            "properties" : {
              "id" : {
                "type" : "long"
              },
              "id_str" : {
                "type" : "string"
              }
            }
          }
        }
      }
    }
  }