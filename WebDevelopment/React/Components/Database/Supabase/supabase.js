//This file creates a client for supabase to use in queries.
//JavaScript

// https://supabase.com/docs/reference/javascript/installing

import { createClient } from '@supabase/supabase-js'

//install "npm install dotenv" to your project to use env
const dotenv = require('dotenv');
dotenv.config();

// Create a single supabase client for interacting with your database
const supabase = createClient(process.env.SUPABASE_CLIENT, process.env.SUPABASE_ANON_KEY)