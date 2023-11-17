import { fastify } from 'fastify' 
import { DatabaseMemory } from './database-memory.js'

const server = fastify()


const database = new DatabaseMemory()

server.post('/videos', (request, reply) => {
    const {title, description, url} = request.body

    

    database.create({
        title,
        description,
        url,
    })

    console.log(database.list())

    return reply.status(201).send()
})

server.get('/videos', () => {
    const videos = database.list()
    
    return videos
})

server.put('/videos/:id', (request, reply) => {
    const videoid = request.params.id
    const {title, description, url} = request.body

    database.update(videoid, {
        title,
        description,
        url,
    })
    return reply.status(204).send()
})

server.listen({
    port: 3333,
})
