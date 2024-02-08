import {client} from './redis_client.js';
//
client.set('key', 'value', (err, reply) => {
    console.log(reply);
}
);

client.get('key', (err, reply) => {
    console.log(reply);
}
);

client.del