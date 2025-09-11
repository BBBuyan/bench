function average_map_func(doc) {
    doc.a1.forEach(function average_map_func(a1) {
        emit(a1.subscribers, a1.total_volume_bytes)
    })
}

function average_map_func(doc) {
    doc.a1.forEach(function average_map_func(a1) {
        a1.a2.forEach(function average_map_func(a2) {
            emit(a2.subscribers, a2.total_volume_bytes)
        })
    })
}

function average_map_func(doc) {
    doc.a1.forEach(function average_map_func(a1) {
        a1.a2.forEach(function average_map_func(a2) {
            a2.a3.forEach(function average_map_func(a3) {
                a3.a4.forEach(function average_map_func(a4) {
                    emit(a4.subscribers, a4.total_volume_bytes)
                })
            })
        })
    })
}

function average_map_func(doc) {
    doc.a1.forEach(function average_map_func(a1) {
        a1.a2.forEach(function average_map_func(a2) {
            a2.a3.forEach(function average_map_func(a3) {
                a3.a4.forEach(function average_map_func(a4) {
                    a4.a5.forEach(function average_map_func(a5) {
                        a5.a6.forEach(function average_map_func(a6) {
                            a6.a7.forEach(function average_map_func(a7) {
                                a7.a8.forEach(function average_map_func(a8) {
                                    emit(a8.subscribers, a8.total_volume_bytes)
                                })
                            })
                        })
                    })
                })
            })
        })
    })
}
