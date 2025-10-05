const routes = [
    { pattern: /^\/api\//,        base: "https://nno0obb-api.fly.dev" },
  ];
  
function getBase(pathname: string) {
  for (const r of routes) if (r.pattern.test(pathname)) return r.base;
  return null;
}
  
export default {
  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);
    const base = getBase(url.pathname);
    if (!base) return new Response("Not found", { status: 404 });
  
    const dest = new URL(base);
    dest.pathname = url.pathname
    dest.search = url.search;
  
    return fetch(dest.toString(), request);
  },
};