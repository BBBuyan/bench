from pprint import pprint
test = {
  "_id": "068cbd9fc208d1e174a46e0af500174a",
  "_rev": "1-a1518596f7dbadc14b4caea4d0b1d4e8",
  "device": 2235,
  "a1": [
    {
      "level": 4756,
      "a2": [
        {
          "level": 6934,
          "a3": [
            {
              "level": 4335,
              "a4": [
                {
                  "device": 3687,
                  "total_volume_bytes": 41,
                  "number_of_records": 469,
                  "subscribers": 6674,
                  "app": "education"
                },
                {
                  "device": 9531,
                  "total_volume_bytes": 3666,
                  "number_of_records": 586,
                  "subscribers": 7805,
                  "app": "leave"
                }
              ]
            },
            {
              "level": 5006,
              "a4": [
                {
                  "device": 8301,
                  "total_volume_bytes": 5283,
                  "number_of_records": 873,
                  "subscribers": 242,
                  "app": "high"
                },
                {
                  "device": 2201,
                  "total_volume_bytes": 1692,
                  "number_of_records": 545,
                  "subscribers": 5328,
                  "app": "star"
                }
              ]
            }
          ]
        },
        {
          "level": 7225,
          "a3": [
            {
              "level": 2667,
              "a4": [
                {
                  "device": 4019,
                  "total_volume_bytes": 260,
                  "number_of_records": 184,
                  "subscribers": 5410,
                  "app": "or"
                },
                {
                  "device": 1581,
                  "total_volume_bytes": 2356,
                  "number_of_records": 627,
                  "subscribers": 8512,
                  "app": "go"
                }
              ]
            },
            {
              "level": 3277,
              "a4": [
                {
                  "device": 8703,
                  "total_volume_bytes": 853,
                  "number_of_records": 544,
                  "subscribers": 7147,
                  "app": "upon"
                },
                {
                  "device": 1600,
                  "total_volume_bytes": 8132,
                  "number_of_records": 574,
                  "subscribers": 886,
                  "app": "morning"
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "level": 5336,
      "a2": [
        {
          "level": 9621,
          "a3": [
            {
              "level": 1920,
              "a4": [
                {
                  "device": 4845,
                  "total_volume_bytes": 9705,
                  "number_of_records": 72,
                  "subscribers": 2343,
                  "app": "itself"
                },
                {
                  "device": 1694,
                  "total_volume_bytes": 8819,
                  "number_of_records": 389,
                  "subscribers": 8068,
                  "app": "president"
                }
              ]
            },
            {
              "level": 9416,
              "a4": [
                {
                  "device": 9275,
                  "total_volume_bytes": 1127,
                  "number_of_records": 695,
                  "subscribers": 4898,
                  "app": "significant"
                },
                {
                  "device": 1786,
                  "total_volume_bytes": 1716,
                  "number_of_records": 829,
                  "subscribers": 9811,
                  "app": "sense"
                }
              ]
            }
          ]
        },
        {
          "level": 3361,
          "a3": [
            {
              "level": 995,
              "a4": [
                {
                  "device": 1800,
                  "total_volume_bytes": 2758,
                  "number_of_records": 259,
                  "subscribers": 120,
                  "app": "social"
                },
                {
                  "device": 5013,
                  "total_volume_bytes": 5945,
                  "number_of_records": 163,
                  "subscribers": 2349,
                  "app": "brother"
                }
              ]
            },
            {
              "level": 6101,
              "a4": [
                {
                  "device": 9130,
                  "total_volume_bytes": 21,
                  "number_of_records": 196,
                  "subscribers": 9132,
                  "app": "close"
                },
                {
                  "device": 8675,
                  "total_volume_bytes": 5513,
                  "number_of_records": 198,
                  "subscribers": 4909,
                  "app": "decide"
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}

# pprint(test["a1"]["a2"])

def update_arr(arr: dict):
    for i in arr["a1"]:
        pprint(i)

update_arr(test)
