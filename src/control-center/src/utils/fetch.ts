import { storeToRefs } from 'pinia'

/** Signature of the browser fetch function. */
export type FetchFunction = (path: string, init?: RequestInit) => Promise<Response>

/** Return true if the given HTTP method is a method that potentially mutates client-visible server state. */
function isMutatingMethod(method: string): boolean {
  const nonMutatingMethods = ['GET', 'HEAD', 'OPTIONS']
  return !nonMutatingMethods.includes(method.toUpperCase())
}

export function getBackendUrl() {
  return "http://localhost:8000"
}

export async function fetchBackend(path: string, init?: RequestInit): Promise<Response> {
  // make sure path starts with a slash.
  path = path.startsWith('/') ? path : '/' + path
  const url = getBackendUrl() + path


  if (isMutatingMethod(init?.method ?? 'GET') ) {
    init = {
      ...init,
      headers: {
        ...init?.headers
      }
    }
  }

  try {
    return await fetch(url, {
      mode: 'cors', // use request headers for cross-origin calls
      ...init
    })
  } catch (err) {
    console.error(`Error fetching '${url}'`, err)
    throw err
  }
}

/**
 * An error that is thrown for any of the JSON functions (such as getJson or postJson) when the response
 * contains an error status code (not 2xx).
 */
export class FetchJsonError extends Error {
  readonly status: number
  constructor(
    public readonly res: Response,
    public readonly body: string
  ) {
    super(`Unexpected '${res.status} ${res.statusText}' response from backend: ${body}`)
    this.status = res.status
  }
}

/**
 * Send a GET request to the given path using the specified Fetch function.
 * Return the result as parsed JSON or null for a 404 error.
 * Throw a FetchJsonError on any other error (non 2xx status)
 */
export async function getJson(
  fetchFn: FetchFunction,
  path: string,
  init?: RequestInit
): Promise<any | null> {
  try {
    return await fetchJson(fetchFn, path, init)
  } catch (err: any) {
    // Special case: return null on 404.
    return err?.status === 404 ? Promise.resolve(null) : Promise.reject(err)
  }
}

/**
 * Send a PUT request to the given path using the specified fetch function.
 * Pass the given data in the body stringified as JSON payload and return the result as parsed JSON.
 * Throw a FetchJsonError on any error (non 2xx status)
 */
export function putJson(
  fetchFn: FetchFunction,
  path: string,
  data: any,
  init?: RequestInit
): Promise<any> {
  return fetchJsonWithPayload(fetchFn, path, 'PUT', data, init)
}

/**
 * Send a PATCH request to the given path using the specified fetch function.
 * Pass the given data in the body stringified as JSON payload and return the result as parsed JSON.
 * Throw a FetchJsonError on any error (non 2xx status).
 */
export function patchJson(
  fetchFn: FetchFunction,
  path: string,
  data: any,
  init?: RequestInit
): Promise<any> {
  return fetchJsonWithPayload(fetchFn, path, 'PATCH', data, init)
}

/**
 * Send a POST request to the given path using the specified fetch function.
 * Pass the given data in the body stringified as JSON payload and return the result as parsed JSON.
 * Throw a FetchJsonError on any error (non 2xx status).
 */
export function postJson<T>(
  fetchFn: FetchFunction,
  path: string,
  data: T,
  init?: RequestInit
): Promise<any> {
  return fetchJsonWithPayload(fetchFn, path, 'POST', data, init)
}

/**
 * Send a DELETE request to the given path using the specified fetch function.
 * Return any result (which admittedly is uncommon for DELETE) as parsed JSON.
 * Throw a FetchJsonError on any error (non 2xx status).
 */
export function deleteJson(fetchFn: FetchFunction, path: string, init?: RequestInit): Promise<any> {
  return fetchJson(fetchFn, path, {
    ...init,
    method: 'DELETE'
  })
}

// Internal functions ---------------------------------------------------------

async function fetchJson(fetchFn: FetchFunction, path: string, init?: RequestInit): Promise<any> {
  const res = await fetchFn(path, {
    ...init,
    headers: {
      Accept: 'application/json',
      ...init?.headers
    }
  })

  const text = (await res.text()).trim()
  if (res.ok) {
    return text.length === 0 ? {} : JSON.parse(text)
  }

  throw new FetchJsonError(res, text)
}

async function fetchJsonWithPayload(
  fetchFn: FetchFunction,
  path: string,
  method: string,
  payload: any,
  init?: RequestInit
): Promise<any> {
  return fetchJson(fetchFn, path, {
    ...init,
    headers: {
      'Content-Type': 'application/json',
      ...init?.headers
    },
    method,
    body: JSON.stringify(payload)
  })
}
