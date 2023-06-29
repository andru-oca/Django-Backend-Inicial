import { createApp } from "https://unpkg.com/vue@3/dist/vue.esm-browser.js";
import { Core } from "./vue.js";
import { config } from "./configvue.js";

const app = createApp(Core);
app.mount(config.PARENT_ID);