const json: Record<string, string>
declare module '*.yaml' {
  export default json
}

declare module '*.yml' {
  export default json
}
