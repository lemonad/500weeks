import sirv from 'sirv';
import polka from 'polka';
import compression from 'compression';
import * as sapper from '../__sapper__/server.js';
import { Store } from 'svelte/store.js';

const { PORT, NODE_ENV } = process.env;
const dev = NODE_ENV === 'development';

const user = {
	name: "Johan",
	email: "jam@learningwell.se",
	biography: "Biagrafi och sånt",
};

polka() // You can also use Express
	.use(
		compression({ threshold: 0 }),
		sirv('static', { dev }),
		sapper.middleware({
      store: () => {
        return new Store({
					newUser: false,
					introStep: 1,
					loggedIn: false,
          user
        });
      }
    })
	)
	.listen(PORT, err => {
		if (err) console.log('error', err);
	});
