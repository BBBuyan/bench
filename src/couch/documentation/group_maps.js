function group_map_func (doc){
  doc.a1.forEach(function(a1){
      emit(a1.subscribers, null)
  })
}

function group_map_func(doc){
  doc.a1.forEach(function(a1){
    a1.a2.foreach(function(a2){
      emit(a2.subscribers, null)
    })
  })
}

function group_map_func(doc) {
    doc.a1.forEach(function(a1) {
        a1.a2.forEach(function(a2) {
            a2.a3.forEach(function(a3) {
                a3.a4.forEach(function(a4) {
                    emit(a4.subscribers, null)
                })
            })
        })
    })
}

function group_map_func(doc) {
    doc.a1.forEach(function(a1) {
        a1.a2.forEach(function(a2) {
            a2.a3.forEach(function(a3) {
                a3.a4.forEach(function(a4) {
                    a4.a5.forEach(function(a5) {
                        a5.a6.forEach(function(a6) {
                            a6.a7.forEach(function(a7) {
                                a7.a8.forEach(function(a8) {
                                    emit(a8.subscribers, null)
                                })
                            })
                        })
                    })
                })
            })
        })
    })
}
