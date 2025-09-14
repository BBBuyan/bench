from elastic_transport import ObjectApiResponse

def show_res(res: ObjectApiResponse):
    for i in res["hits"]["hits"]:
        print(i["_source"])
        print("--------")
    print(f"{'es took':<20}: {res["took"]} ms")
    print(f"{'count':<20}: {res["hits"]["total"]["value"]}")
