export const ACCEPTED_MEDIA_TYPES = ["image/*", "video/*", "application/pdf"];

export const ACCEPT_ATTRIBUTE = ACCEPTED_MEDIA_TYPES.join(",");

export const UNSUPPORTED_FILE_MESSAGE =
  "Unsupported file type. Please choose an image, video, or PDF file.";

export function isSupportedMediaFile(file) {
  if (!file?.type) {
    return false;
  }

  return ACCEPTED_MEDIA_TYPES.some((accepted) =>
    accepted.endsWith("/*")
      ? file.type.startsWith(accepted.slice(0, -1))
      : file.type === accepted
  );
}
