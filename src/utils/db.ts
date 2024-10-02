import { Pool, QueryResult, QueryResultRow } from 'pg';

const pool = new Pool({
  user: process.env["DB_USER"],
  host: process.env["DB_HOST"],
  database: process.env["DB_NAME"],
  password: process.env["DB_PASSWORD"],
  port: parseInt(process.env["DB_PORT"])
});

type QueryFunction = <T extends QueryResultRow = any>(text: string, params?: any[]) => Promise<QueryResult<T>>;

const query: QueryFunction = (text, params) => pool.query(text, params);

export { query, pool };
