package communicationmod;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.BlockingQueue;

public class DataReader implements Runnable{

    private final BlockingQueue<String> queue;
    private final BufferedReader reader;
    private static final Logger logger = LogManager.getLogger(DataReader.class.getName());
    private boolean verbose;

    public DataReader (BlockingQueue<String> queue, InputStream stream, boolean verbose) {
        this.queue = queue;
        this.reader = new BufferedReader(new InputStreamReader(stream, StandardCharsets.UTF_8));
        this.verbose = verbose;
    }

    public void run() {
        while (!Thread.currentThread().isInterrupted()) {
            try {
                String line = reader.readLine();
                if (line == null) {
                    continue;
                }
                if (line.length() > 0) {
                    if (verbose) {
                        logger.info("Received message: " + line);
                    }
                    queue.put(line);
                }
            } catch(IOException e){
                logger.error("Message could not be received from child process. Shutting down reading thread.");
                Thread.currentThread().interrupt();
            } catch(InterruptedException e) {
                logger.info("Communications reading thread interrupted.");
                Thread.currentThread().interrupt();
            }
        }
    }
}
