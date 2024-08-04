const express = require('express')

const app = express()
const port = 3000

/**
 * GET
 * POST
 * DELETE
 * PUT PATCH
 */

app.get('/', (req, res) => {
    res.send("APP GET")
})

app.post('/', (req, res) => {
    res.send("APP POST!")
})

app.delete('/', (req, res) => {
    res.send("APP DELETE")
})

app.listen(port, () => {
    console.log(`App online na porta ${port}`)
})


