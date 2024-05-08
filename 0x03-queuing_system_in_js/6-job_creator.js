import { createQueue } from 'kue';

const queue = createQueue();

const notify = {
  'phoneNumber': '4153518780',
  'message': 'This is the code to verify your account',
}

const job = queue.create('push_notification_code', notify).save(function (err) {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('completed', () => {
  console.log('Notification job completed');
});.on('failed', () => {
  console.log('Notification job failed');
});
