const API_HOST: string = import.meta.env.VITE_API_URL;

export const getApiPath = (path: string): string => {
  if (path[0] != "/") {
    throw Error("paths must start with '/'");
  }
  return API_HOST + path;
};
